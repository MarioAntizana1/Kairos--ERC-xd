"""Launch the mission node against an already running Nav2 stack."""

from __future__ import annotations

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    mission_dir = get_package_share_directory("rover_mission")
    default_waypoints = os.path.join(mission_dir, "config", "waypoints_demo.yaml")

    waypoints = LaunchConfiguration("waypoints")
    auto_start = LaunchConfiguration("auto_start")
    use_sim_time = LaunchConfiguration("use_sim_time")
    max_retries = LaunchConfiguration("max_retries")
    goal_timeout_s = LaunchConfiguration("goal_timeout_s")

    mission_node = Node(
        package="rover_mission",
        executable="mission_node",
        name="mission_node",
        parameters=[{
            "waypoints_file": waypoints,
            "auto_start": auto_start,
            "max_retries": max_retries,
            "goal_timeout_s": goal_timeout_s,
            "use_sim_time": use_sim_time,
        }],
        output="screen",
    )

    return LaunchDescription([
        DeclareLaunchArgument("waypoints", default_value=default_waypoints),
        DeclareLaunchArgument("auto_start", default_value="false"),
        DeclareLaunchArgument("use_sim_time", default_value="true"),
        DeclareLaunchArgument("max_retries", default_value="1"),
        DeclareLaunchArgument("goal_timeout_s", default_value="120.0"),
        mission_node,
    ])
