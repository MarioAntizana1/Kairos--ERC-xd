cmake_minimum_required(VERSION 3.8)
project(rover_bringup)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch config maps worlds
  DESTINATION share/${PROJECT_NAME}
)

install(
  PROGRAMS scripts/odom_tf_broadcaster.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
