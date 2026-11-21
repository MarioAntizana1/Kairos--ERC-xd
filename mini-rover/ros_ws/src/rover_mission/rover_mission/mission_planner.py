"""Pure mission state machine, independent of ROS.

Keeping this module free of rclpy lets the mission logic run under plain
Python (unit tests, CI, documentation builds) and keeps the ROS node thin.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from typing import Any, Iterable


class MissionState(str, Enum):
    """Lifecycle of a mission."""

    IDLE = "IDLE"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    COMPLETED = "COMPLETED"
    COMPLETED_WITH_WARNING = "COMPLETED_WITH_WARNING"
    FAILED = "FAILED"
    ABORTED = "ABORTED"
    BATTERY_LOW = "BATTERY_LOW"

    @property
    def is_terminal(self) -> bool:
        return self in {
            MissionState.COMPLETED,
            MissionState.COMPLETED_WITH_WARNING,
            MissionState.FAILED,
            MissionState.ABORTED,
            MissionState.BATTERY_LOW,
        }


def _finite_number(value: Any, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a number")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


@dataclass(frozen=True)
class Waypoint:
    """A single mission waypoint in the map frame."""

    id: str
    x: float
    y: float
    yaw: float = 0.0
    tolerance: float = 0.25
    timeout_s: float = 90.0

    def validate(self) -> None:
        if not isinstance(self.id, str) or not self.id.strip():
            raise ValueError("waypoint id must be a non-empty string")
        _finite_number(self.x, f"{self.id}.x")
        _finite_number(self.y, f"{self.id}.y")
        _finite_number(self.yaw, f"{self.id}.yaw")
        tolerance = _finite_number(self.tolerance, f"{self.id}.tolerance")
        timeout = _finite_number(self.timeout_s, f"{self.id}.timeout_s")
        if tolerance <= 0:
            raise ValueError(f"{self.id}.tolerance must be positive")
        if timeout <= 0:
            raise ValueError(f"{self.id}.timeout_s must be positive")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Waypoint":
        if not isinstance(data, dict):
            raise ValueError("waypoint must be an object")
        if "id" not in data:
            raise ValueError("waypoint is missing 'id'")
        if "x" not in data or "y" not in data:
            raise ValueError(f"waypoint {data.get('id')!r} is missing x/y")
        waypoint = cls(
            id=data["id"],
            x=_finite_number(data["x"], f"{data['id']}.x"),
            y=_finite_number(data["y"], f"{data['id']}.y"),
            yaw=_finite_number(data.get("yaw", 0.0), f"{data['id']}.yaw"),
            tolerance=_finite_number(data.get("tolerance", 0.25), f"{data['id']}.tolerance"),
            timeout_s=_finite_number(data.get("timeout_s", 90.0), f"{data['id']}.timeout_s"),
        )
        waypoint.validate()
        return waypoint

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "yaw": self.yaw,
            "tolerance": self.tolerance,
            "timeout_s": self.timeout_s,
        }


class MissionPlanner:
    """Sequential waypoint state machine with retries and abort/resume."""

    def __init__(
        self,
        waypoints: Iterable[Waypoint],
        max_retries: int = 1,
        loop: bool = False,
        return_to_base: bool = False,
    ) -> None:
        self._waypoints = list(waypoints)
        if not self._waypoints:
            raise ValueError("mission must contain at least one waypoint")
        for waypoint in self._waypoints:
            if not isinstance(waypoint, Waypoint):
                raise TypeError("waypoints must be Waypoint instances")
            waypoint.validate()

        ids = [waypoint.id for waypoint in self._waypoints]
        if len(set(ids)) != len(ids):
            duplicates = sorted({item for item in ids if ids.count(item) > 1})
            raise ValueError(f"duplicate waypoint id(s): {', '.join(duplicates)}")

        if isinstance(max_retries, bool) or not isinstance(max_retries, int):
            raise ValueError("max_retries must be an integer")
        if max_retries < 0:
            raise ValueError("max_retries must be >= 0")
        if return_to_base and "BASE" not in ids:
            raise ValueError("return_to_base requires a waypoint with id 'BASE'")
        if return_to_base and self._waypoints[-1].id != "BASE":
            raise ValueError("return_to_base requires 'BASE' to be the last waypoint")

        self._max_retries = max_retries
        self._loop = bool(loop)
        self._return_to_base = bool(return_to_base)
        self._state = MissionState.IDLE
        self._index = 0
        self._attempts = 0
        self._reached: list[str] = []
        self._failed: list[str] = []
        self._abort_reason: str | None = None
        self._last_error: str | None = None

    # ------------------------------------------------------------------
    # Read-only properties
    # ------------------------------------------------------------------
    @property
    def state(self) -> MissionState:
        return self._state

    @property
    def waypoints(self) -> tuple[Waypoint, ...]:
        return tuple(self._waypoints)

    @property
    def index(self) -> int:
        return self._index

    @property
    def attempts(self) -> int:
        return self._attempts

    @property
    def max_retries(self) -> int:
        return self._max_retries

    @property
    def loop(self) -> bool:
        return self._loop

    @property
    def return_to_base(self) -> bool:
        return self._return_to_base

    @property
    def reached(self) -> tuple[str, ...]:
        return tuple(self._reached)

    @property
    def failed(self) -> tuple[str, ...]:
        return tuple(self._failed)

    @property
    def abort_reason(self) -> str | None:
        return self._abort_reason

    @property
    def last_error(self) -> str | None:
        return self._last_error

    @property
    def current_waypoint(self) -> Waypoint | None:
        if self._index >= len(self._waypoints):
            return None
        return self._waypoints[self._index]

    @property
    def remaining_waypoints(self) -> tuple[Waypoint, ...]:
        return tuple(self._waypoints[self._index:])

    @property
    def progress(self) -> float:
        if not self._waypoints:
            return 0.0
        return min(len(self._reached) / len(self._waypoints), 1.0)

    # ------------------------------------------------------------------
    # Transitions
    # ------------------------------------------------------------------
    def start(self) -> MissionState:
        if self._state is not MissionState.IDLE:
            raise RuntimeError(f"cannot start from {self._state.value}")
        self._state = MissionState.RUNNING
        self._abort_reason = None
        return self._state

    def pause(self) -> MissionState:
        if self._state is not MissionState.RUNNING:
            raise RuntimeError(f"cannot pause from {self._state.value}")
        self._state = MissionState.PAUSED
        return self._state

    def resume(self) -> MissionState:
        if self._state not in {MissionState.PAUSED, MissionState.ABORTED}:
            raise RuntimeError(f"cannot resume from {self._state.value}")
        self._state = MissionState.RUNNING
        self._abort_reason = None
        return self._state

    def mark_reached(self) -> MissionState:
        if self._state not in {MissionState.RUNNING, MissionState.PAUSED}:
            raise RuntimeError(f"cannot advance from {self._state.value}")
        waypoint = self.current_waypoint
        if waypoint is None:
            raise RuntimeError("no current waypoint to mark as reached")

        was_paused = self._state is MissionState.PAUSED
        self._reached.append(waypoint.id)
        self._attempts = 0
        self._index += 1

        if self._index >= len(self._waypoints):
            if self._loop:
                self._index = 0
                self._state = MissionState.PAUSED if was_paused else MissionState.RUNNING
            else:
                self._state = MissionState.COMPLETED
        else:
            self._state = MissionState.PAUSED if was_paused else MissionState.RUNNING
        return self._state

    def mark_failed(self, reason: str = "navigation failed") -> bool:
        """Record a failed attempt.

        Returns True if the waypoint will be retried, False if the mission
        transitioned to FAILED.
        """
        if self._state not in {MissionState.RUNNING, MissionState.PAUSED}:
            raise RuntimeError(f"cannot fail from {self._state.value}")
        waypoint = self.current_waypoint
        if waypoint is None:
            raise RuntimeError("no current waypoint to mark as failed")

        self._attempts += 1
        self._last_error = str(reason) if reason else "navigation failed"
        if self._attempts <= self._max_retries:
            return True

        self._failed.append(waypoint.id)
        self._state = MissionState.FAILED
        return False

    def abort(self, reason: str = "operator abort") -> bool:
        if self._state.is_terminal:
            return False
        self._abort_reason = str(reason) if reason else "operator abort"
        self._state = MissionState.ABORTED
        return True

    def mark_battery_low(self, reason: str = "battery voltage below threshold") -> bool:
        if self._state.is_terminal:
            return False
        self._abort_reason = str(reason) if reason else "battery low"
        self._state = MissionState.BATTERY_LOW
        return True

    def complete_with_warning(self, reason: str = "return to base failed") -> bool:
        if self._state is not MissionState.COMPLETED:
            return False
        self._abort_reason = str(reason) if reason else "return to base failed"
        self._state = MissionState.COMPLETED_WITH_WARNING
        return True

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------
    def summary(self) -> dict[str, Any]:
        return {
            "state": self._state.value,
            "total_waypoints": len(self._waypoints),
            "reached": list(self._reached),
            "failed": list(self._failed),
            "attempts": self._attempts,
            "abort_reason": self._abort_reason,
            "last_error": self._last_error,
            "progress": round(self.progress, 4),
            "loop": self._loop,
            "return_to_base": self._return_to_base,
        }
