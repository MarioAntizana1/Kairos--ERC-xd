#!/usr/bin/env python3
"""Publish odom -> base_footprint from a nav_msgs/Odometry topic.

Gazebo's DiffDrive system publishes odometry and a Gazebo-transport TF topic,
but that TF is not automatically bridged to ROS. This node closes the TF tree
in simulation. On hardware, the base driver is expected to publish the same
transform (disable this node in that case).
"""

from __future__ import annotations

import rclpy
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry
from rclpy.node import Node
from tf2_ros import TransformBroadcaster


class OdomTfBroadcaster(Node):
    def __init__(self) -> None:
        super().__init__("odom_tf_broadcaster")
        self.declare_parameter("odom_topic", "odom")
        self.declare_parameter("parent_frame", "odom")
        self.declare_parameter("child_frame", "base_footprint")

        self._parent = self.get_parameter("parent_frame").value
        self._child = self.get_parameter("child_frame").value
        self._broadcaster = TransformBroadcaster(self)
        self._sub = self.create_subscription(
            Odometry,
            self.get_parameter("odom_topic").value,
            self._on_odom,
            20,
        )
        self._logged = False
        self.get_logger().info(
            f"Broadcasting {self._parent} -> {self._child} from odometry"
        )

    def _on_odom(self, msg: Odometry) -> None:
        transform = TransformStamped()
        transform.header.stamp = msg.header.stamp
        transform.header.frame_id = self._parent
        transform.child_frame_id = self._child
        transform.transform.translation.x = msg.pose.pose.position.x
        transform.transform.translation.y = msg.pose.pose.position.y
        transform.transform.translation.z = msg.pose.pose.position.z
        transform.transform.rotation = msg.pose.pose.orientation
        self._broadcaster.sendTransform(transform)
        if not self._logged:
            self._logged = True
            self.get_logger().info("First odometry message received; TF is active")


def main(args: list[str] | None = None) -> None:
    rclpy.init(args=args)
    node = OdomTfBroadcaster()
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
