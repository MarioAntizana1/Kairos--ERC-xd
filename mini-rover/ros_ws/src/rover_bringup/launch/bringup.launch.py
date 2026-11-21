"""Hardware bringup skeleton.

This launch starts the robot description, Nav2 and (optionally) RViz. The
LiDAR, IMU and motor drivers are hardware-specific and must be started
separately (or added here once the components are selected).

It intentionally does not start Gazebo and defaults to use_sim_time=false.
"""

from __future__ import annotations

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description() -> LaunchDescription:
    bringup_dir = get_package_share_directory("rover_bringup")
    description_dir = get_package_share_directory("rover_description")
    nav2_dir = get_package_share_directory("nav2_bringup")

    default_map = os.path.join(bringup_dir, "maps", "mini_marsyard.yaml")
    default_params = os.path.join(bringup_dir, "config", "nav2_params.yaml")
    default_rviz = os.path.join(bringup_dir, "config", "rover.rviz")
    urdf_path = os.path.join(description_dir, "urdf", "rover.urdf.xacro")

    map_yaml = LaunchConfiguration("map")
    params_file = LaunchConfiguration("params_file")
    rviz_config = LaunchConfiguration("rviz_config")
    use_sim_time = LaunchConfiguration("use_sim_time")
    rviz = LaunchConfiguration("rviz")
    autostart = LaunchConfiguration("autostart")
    odom_broadcaster = LaunchConfiguration("odom_tf_broadcaster")

    robot_description = ParameterValue(Command(["xacro ", urdf_path]), value_type=str)

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description, "use_sim_time": use_sim_time}],
        output="screen",
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_dir, "launch", "bringup_launch.py")
        ),
        launch_arguments={
            "map": map_yaml,
            "use_sim_time": use_sim_time,
            "params_file": params_file,
            "autostart": autostart,
            "use_composition": "false",
            "slam": "False",
            "use_localization": "True",
        }.items(),
    )

    odom_tf = Node(
        package="rover_bringup",
        executable="odom_tf_broadcaster.py",
        condition=IfCondition(odom_broadcaster),
        output="screen",
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", rviz_config],
        condition=IfCondition(rviz),
        output="screen",
    )

    return LaunchDescription([
        DeclareLaunchArgument("map", default_value=default_map),
        DeclareLaunchArgument("params_file", default_value=default_params),
        DeclareLaunchArgument("rviz_config", default_value=default_rviz),
        DeclareLaunchArgument("use_sim_time", default_value="false"),
        DeclareLaunchArgument("rviz", default_value="true"),
        DeclareLaunchArgument("autostart", default_value="true"),
        DeclareLaunchArgument(
            "odom_tf_broadcaster",
            default_value="false",
            description="Enable only if the base driver does not publish odom -> base_footprint",
        ),
        robot_state_publisher,
        odom_tf,
        nav2,
        rviz_node,
    ])
