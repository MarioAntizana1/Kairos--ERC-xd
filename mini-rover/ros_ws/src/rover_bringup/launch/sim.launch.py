"""Launch Gazebo, Nav2, RViz and the bridges for the rover simulation."""

from __future__ import annotations

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description() -> LaunchDescription:
    bringup_dir = get_package_share_directory("rover_bringup")
    description_dir = get_package_share_directory("rover_description")
    nav2_dir = get_package_share_directory("nav2_bringup")
    ros_gz_sim_dir = get_package_share_directory("ros_gz_sim")

    default_world = os.path.join(bringup_dir, "worlds", "mini_marsyard.sdf")
    default_map = os.path.join(bringup_dir, "maps", "mini_marsyard.yaml")
    default_params = os.path.join(bringup_dir, "config", "nav2_params.yaml")
    default_rviz = os.path.join(bringup_dir, "config", "rover.rviz")
    urdf_path = os.path.join(description_dir, "urdf", "rover.urdf.xacro")

    world = LaunchConfiguration("world")
    map_yaml = LaunchConfiguration("map")
    params_file = LaunchConfiguration("params_file")
    rviz_config = LaunchConfiguration("rviz_config")
    use_sim_time = LaunchConfiguration("use_sim_time")
    headless = LaunchConfiguration("headless")
    rviz = LaunchConfiguration("rviz")
    autostart = LaunchConfiguration("autostart")
    use_composition = LaunchConfiguration("use_composition")

    robot_description = ParameterValue(Command(["xacro ", urdf_path]), value_type=str)

    gz_sim_gui = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_dir, "launch", "gz_sim.launch.py")
        ),
        launch_arguments={"gz_args": ["-r -v4 ", world]}.items(),
        condition=IfCondition(PythonExpression(["not ", headless])),
    )

    gz_sim_headless = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_dir, "launch", "gz_sim.launch.py")
        ),
        launch_arguments={"gz_args": ["-r -v4 -s ", world]}.items(),
        condition=IfCondition(headless),
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description, "use_sim_time": use_sim_time}],
        output="screen",
    )

    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-topic", "robot_description",
            "-name", "rover",
            "-x", "0.0",
            "-y", "0.0",
            "-z", "0.02",
            "-Y", "0.0",
        ],
        output="screen",
    )

    bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock",
            "/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan",
            "/imu@sensor_msgs/msg/Imu[gz.msgs.IMU",
            "/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry",
            "/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model",
            "/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist",
        ],
        output="screen",
    )

    odom_tf = Node(
        package="rover_bringup",
        executable="odom_tf_broadcaster.py",
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
            "use_composition": use_composition,
            "slam": "False",
            "use_localization": "True",
        }.items(),
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", rviz_config],
        condition=IfCondition(rviz),
        output="screen",
    )

    return LaunchDescription([
        DeclareLaunchArgument("world", default_value=default_world),
        DeclareLaunchArgument("map", default_value=default_map),
        DeclareLaunchArgument("params_file", default_value=default_params),
        DeclareLaunchArgument("rviz_config", default_value=default_rviz),
        DeclareLaunchArgument("use_sim_time", default_value="true"),
        DeclareLaunchArgument("headless", default_value="false"),
        DeclareLaunchArgument("rviz", default_value="true"),
        DeclareLaunchArgument("autostart", default_value="true"),
        DeclareLaunchArgument("use_composition", default_value="false"),
        gz_sim_gui,
        gz_sim_headless,
        robot_state_publisher,
        bridge,
        odom_tf,
        TimerAction(period=3.0, actions=[spawn_robot]),
        nav2,
        rviz_node,
    ])
