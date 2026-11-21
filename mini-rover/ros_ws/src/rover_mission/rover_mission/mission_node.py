"""ROS 2 node that orchestrates a waypoint mission through Nav2."""

from __future__ import annotations

import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import rclpy
from action_msgs.msg import GoalStatus
from ament_index_python.packages import get_package_share_directory
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy, HistoryPolicy, QoSProfile, ReliabilityPolicy
from std_msgs.msg import Float32, String
from std_srvs.srv import Trigger

from .mission_planner import MissionPlanner, MissionState
from .waypoints import load_mission


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _yaw_to_quaternion(yaw: float) -> tuple[float, float, float, float]:
    return (0.0, 0.0, math.sin(yaw / 2.0), math.cos(yaw / 2.0))


class MissionNode(Node):
    """Thin ROS wrapper around MissionPlanner and Nav2's NavigateToPose."""

    def __init__(self) -> None:
        super().__init__("mission_node")

        self.declare_parameter("use_sim_time", False)
        self.declare_parameter("waypoints_file", "waypoints_demo.yaml")
        self.declare_parameter("auto_start", False)
        self.declare_parameter("max_retries", 1)
        self.declare_parameter("goal_timeout_s", 120.0)
        self.declare_parameter("feedback_timeout_s", 10.0)
        self.declare_parameter("status_rate_hz", 2.0)

        self._goal_timeout_s = float(self.get_parameter("goal_timeout_s").value)
        self._feedback_timeout_s = float(self.get_parameter("feedback_timeout_s").value)
        status_rate = float(self.get_parameter("status_rate_hz").value)
        if status_rate <= 0:
            status_rate = 2.0

        self._planner: MissionPlanner | None = None
        self._frame_id = "map"
        self._load_error: str | None = None
        self._load_mission()

        self._client = ActionClient(self, NavigateToPose, "navigate_to_pose")

        summary_qos = QoSProfile(
            depth=1,
            history=HistoryPolicy.KEEP_LAST,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            reliability=ReliabilityPolicy.RELIABLE,
        )
        self._status_pub = self.create_publisher(String, "/rover/mission/status", 10)
        self._progress_pub = self.create_publisher(Float32, "/rover/mission/progress", 10)
        self._summary_pub = self.create_publisher(String, "/rover/mission/summary", summary_qos)

        self.create_service(Trigger, "/rover/mission/start", self._handle_start)
        self.create_service(Trigger, "/rover/mission/abort", self._handle_abort)
        self.create_service(Trigger, "/rover/mission/pause", self._handle_pause)
        self.create_service(Trigger, "/rover/mission/resume", self._handle_resume)

        self._phase = "IDLE"
        self._send_future = None
        self._result_future = None
        self._goal_handle = None
        self._deadline = 0.0
        self._cancel_deadline = 0.0
        self._last_feedback_at = 0.0
        self._mission_id = ""
        self._started_monotonic: float | None = None
        self._started_iso: str | None = None
        self._finished_iso: str | None = None
        self._summary_published = False
        self._last_message = "idle"
        self._auto_start_pending = bool(self.get_parameter("auto_start").value)

        self.create_timer(0.1, self._tick)
        self.create_timer(1.0 / status_rate, self._publish_status)

        if self._planner is not None:
            self.get_logger().info(
                f"Loaded mission with {len(self._planner.waypoints)} waypoints "
                f"in frame '{self._frame_id}'"
            )
        else:
            self.get_logger().error(f"Mission not loaded: {self._load_error}")

    # ------------------------------------------------------------------
    # Setup helpers
    # ------------------------------------------------------------------
    def _load_mission(self) -> None:
        raw = str(self.get_parameter("waypoints_file").value)
        try:
            path = Path(raw).expanduser()
            if not path.is_absolute():
                path = Path(get_package_share_directory("rover_mission")) / "config" / path
            self._planner, self._frame_id = load_mission(
                path,
                max_retries=int(self.get_parameter("max_retries").value),
            )
        except Exception as exc:  # noqa: BLE001 - surface the error to the operator
            self._planner = None
            self._load_error = str(exc)

    # ------------------------------------------------------------------
    # Services
    # ------------------------------------------------------------------
    def _handle_start(self, _request: Trigger.Request, response: Trigger.Response) -> Trigger.Response:
        ok, message = self._start_mission()
        response.success = ok
        response.message = message
        return response

    def _handle_abort(self, _request: Trigger.Request, response: Trigger.Response) -> Trigger.Response:
        if self._planner is None:
            response.success = False
            response.message = self._load_error or "mission not loaded"
            return response
        if not self._planner.abort("operator abort"):
            response.success = False
            response.message = f"cannot abort from {self._planner.state.value}"
            return response

        if self._goal_handle is not None:
            self._goal_handle.cancel_goal_async()
        self._reset_action_state()
        self._last_message = "aborted by operator"
        self.get_logger().warn("Mission aborted by operator")
        self._finish_mission()
        response.success = True
        response.message = "mission aborted"
        return response

    def _handle_pause(self, _request: Trigger.Request, response: Trigger.Response) -> Trigger.Response:
        if self._planner is None:
            response.success = False
            response.message = self._load_error or "mission not loaded"
            return response
        try:
            self._planner.pause()
        except RuntimeError as exc:
            response.success = False
            response.message = str(exc)
            return response
        self._last_message = "paused"
        response.success = True
        response.message = "mission paused after the current waypoint"
        return response

    def _handle_resume(self, _request: Trigger.Request, response: Trigger.Response) -> Trigger.Response:
        if self._planner is None:
            response.success = False
            response.message = self._load_error or "mission not loaded"
            return response
        try:
            self._planner.resume()
        except RuntimeError as exc:
            response.success = False
            response.message = str(exc)
            return response
        self._summary_published = False
        self._finished_iso = None
        self._last_message = "resumed"
        response.success = True
        response.message = "mission resumed"
        return response

    # ------------------------------------------------------------------
    # Mission lifecycle
    # ------------------------------------------------------------------
    def _start_mission(self) -> tuple[bool, str]:
        if self._planner is None:
            return False, self._load_error or "mission not loaded"
        if self._planner.state is not MissionState.IDLE:
            return False, f"cannot start from {self._planner.state.value}"
        if not self._client.server_is_ready():
            return False, "navigate_to_pose action server is not ready"

        try:
            self._planner.start()
        except RuntimeError as exc:
            return False, str(exc)

        self._mission_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        self._started_monotonic = time.monotonic()
        self._started_iso = _now_iso()
        self._finished_iso = None
        self._summary_published = False
        self._last_message = "mission started"
        self._reset_action_state()
        self.get_logger().info(f"Mission {self._mission_id} started")
        return True, "mission started"

    def _finish_mission(self) -> None:
        if self._summary_published or self._planner is None:
            return
        self._summary_published = True
        self._finished_iso = _now_iso()
        duration = 0.0
        if self._started_monotonic is not None:
            duration = round(time.monotonic() - self._started_monotonic, 3)

        summary: dict[str, Any] = self._planner.summary()
        summary.update({
            "mission_id": self._mission_id,
            "started_at": self._started_iso,
            "finished_at": self._finished_iso,
            "duration_s": duration,
        })
        self._summary_pub.publish(String(data=json.dumps(summary)))
        self.get_logger().info(f"Mission finished: {summary['state']} ({duration:.1f} s)")

    def _reset_action_state(self) -> None:
        self._phase = "IDLE"
        self._send_future = None
        self._result_future = None
        self._goal_handle = None
        self._deadline = 0.0
        self._cancel_deadline = 0.0

    # ------------------------------------------------------------------
    # Timer callbacks
    # ------------------------------------------------------------------
    def _tick(self) -> None:
        if self._planner is None:
            return

        if self._auto_start_pending and self._planner.state is MissionState.IDLE:
            if self._client.server_is_ready():
                ok, message = self._start_mission()
                self._auto_start_pending = False
                if not ok:
                    self.get_logger().warning(f"Auto-start failed: {message}")

        if self._planner.state is not MissionState.RUNNING:
            return

        now = time.monotonic()
        if self._phase == "IDLE":
            self._send_next_goal()
        elif self._phase == "SENDING":
            self._handle_sending()
        elif self._phase == "NAVIGATING":
            self._handle_navigating(now)
        elif self._phase == "CANCELLING":
            self._handle_cancelling(now)

    def _send_next_goal(self) -> None:
        if self._planner is None:
            return
        waypoint = self._planner.current_waypoint
        if waypoint is None:
            return

        goal = NavigateToPose.Goal()
        goal.pose.header.frame_id = self._frame_id
        goal.pose.header.stamp = self.get_clock().now().to_msg()
        goal.pose.pose.position.x = waypoint.x
        goal.pose.pose.position.y = waypoint.y
        goal.pose.pose.position.z = 0.0
        qx, qy, qz, qw = _yaw_to_quaternion(waypoint.yaw)
        goal.pose.pose.orientation.x = qx
        goal.pose.pose.orientation.y = qy
        goal.pose.pose.orientation.z = qz
        goal.pose.pose.orientation.w = qw

        self._send_future = self._client.send_goal_async(
            goal, feedback_callback=self._feedback_callback
        )
        self._phase = "SENDING"
        self._last_feedback_at = time.monotonic()
        self._last_message = f"sending {waypoint.id}"
        self.get_logger().info(f"Sending waypoint {waypoint.id}")

    def _handle_sending(self) -> None:
        if self._send_future is None or not self._send_future.done():
            return
        goal_handle = self._send_future.result()
        self._send_future = None

        if goal_handle is None or not goal_handle.accepted:
            self._phase = "IDLE"
            self._handle_failure("goal rejected by action server")
            return

        self._goal_handle = goal_handle
        self._result_future = goal_handle.get_result_async()
        self._phase = "NAVIGATING"
        waypoint = self._planner.current_waypoint if self._planner else None
        timeout = waypoint.timeout_s if waypoint else self._goal_timeout_s
        self._deadline = time.monotonic() + max(timeout, 1.0)
        self._last_feedback_at = time.monotonic()
        self._last_message = f"navigating to {waypoint.id if waypoint else '?'}"

    def _handle_navigating(self, now: float) -> None:
        if self._result_future is not None and self._result_future.done():
            result = self._result_future.result()
            status = result.status
            self._reset_action_state()
            if status == GoalStatus.STATUS_SUCCEEDED:
                self._on_waypoint_reached()
            else:
                self._handle_failure(f"navigation finished with status {status}")
            return

        if now > self._deadline:
            self._start_cancel("goal timeout")
        elif now - self._last_feedback_at > self._feedback_timeout_s:
            self._start_cancel("feedback timeout")

    def _start_cancel(self, reason: str) -> None:
        if self._goal_handle is not None:
            self._goal_handle.cancel_goal_async()
        self._phase = "CANCELLING"
        self._cancel_deadline = time.monotonic() + 5.0
        self._last_message = f"cancelling: {reason}"
        self.get_logger().warning(f"Cancelling navigation: {reason}")

    def _handle_cancelling(self, now: float) -> None:
        if self._result_future is not None and self._result_future.done():
            self._result_future.result()
            self._reset_action_state()
            self._handle_failure("navigation cancelled after timeout")
        elif now > self._cancel_deadline:
            self._reset_action_state()
            self._handle_failure("cancel did not complete in time")

    def _feedback_callback(self, feedback_msg: Any) -> None:
        self._last_feedback_at = time.monotonic()
        if self._planner is None:
            return
        waypoint = self._planner.current_waypoint
        if waypoint is None:
            return
        try:
            distance = float(feedback_msg.feedback.distance_remaining)
            self._last_message = f"navigating to {waypoint.id}: {distance:.2f} m remaining"
        except Exception:  # noqa: BLE001 - feedback is optional
            self._last_message = f"navigating to {waypoint.id}"

    def _on_waypoint_reached(self) -> None:
        if self._planner is None:
            return
        waypoint = self._planner.current_waypoint
        waypoint_id = waypoint.id if waypoint else "?"
        try:
            state = self._planner.mark_reached()
        except RuntimeError as exc:
            self.get_logger().error(f"Could not advance mission: {exc}")
            self._finish_mission()
            return

        self.get_logger().info(f"Reached waypoint {waypoint_id}")
        self._last_message = f"reached {waypoint_id}"
        if state is MissionState.COMPLETED:
            self._finish_mission()
        elif state is MissionState.PAUSED:
            self._last_message = f"paused after {waypoint_id}"

    def _handle_failure(self, reason: str) -> None:
        if self._planner is None:
            return
        retry = self._planner.mark_failed(reason)
        if retry:
            waypoint = self._planner.current_waypoint
            self._last_message = f"retrying {waypoint.id if waypoint else '?'}: {reason}"
            self.get_logger().warning(self._last_message)
        else:
            self._last_message = f"mission failed: {reason}"
            self.get_logger().error(self._last_message)
            self._finish_mission()

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------
    def _publish_status(self) -> None:
        if self._planner is None:
            status = {
                "state": MissionState.IDLE.value,
                "mission_id": None,
                "frame_id": self._frame_id,
                "current_waypoint": None,
                "index": 0,
                "total": 0,
                "progress": 0.0,
                "attempts": 0,
                "message": self._load_error or "mission not loaded",
                "timestamp": _now_iso(),
            }
            progress = 0.0
        else:
            waypoint = self._planner.current_waypoint
            status = {
                "state": self._planner.state.value,
                "mission_id": self._mission_id or None,
                "frame_id": self._frame_id,
                "current_waypoint": waypoint.id if waypoint else None,
                "index": self._planner.index,
                "total": len(self._planner.waypoints),
                "progress": round(self._planner.progress, 4),
                "attempts": self._planner.attempts,
                "message": self._last_message,
                "timestamp": _now_iso(),
            }
            progress = self._planner.progress

        self._status_pub.publish(String(data=json.dumps(status)))
        self._progress_pub.publish(Float32(data=float(progress)))


def main(args: list[str] | None = None) -> None:
    rclpy.init(args=args)
    node = MissionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
