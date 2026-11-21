#!/usr/bin/env bash
# Build the ROS 2 workspace with colcon.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CLEAN=false
ARGS=()

for arg in "$@"; do
  case "$arg" in
    --clean) CLEAN=true ;;
    *) ARGS+=("$arg") ;;
  esac
done

if ! command -v ros2 >/dev/null 2>&1; then
  echo "ERROR: ROS 2 is not available in this shell." >&2
  echo "Source /opt/ros/jazzy/setup.bash or use an Ubuntu 24.04 environment." >&2
  exit 1
fi

# shellcheck disable=SC1090
source "/opt/ros/${ROS_DISTRO:-jazzy}/setup.bash"

if ! command -v colcon >/dev/null 2>&1; then
  echo "ERROR: colcon is not installed. Install ros-dev-tools." >&2
  exit 1
fi

cd "$ROOT/ros_ws"

if [ "$CLEAN" = true ]; then
  echo "== Cleaning build/install/log =="
  rm -rf build install log
fi

echo "== Installing dependencies with rosdep =="
rosdep install --from-paths src --ignore-src -r -y

echo "== Building with colcon =="
colcon build --symlink-install "${ARGS[@]}"

echo
echo "Build finished. In this shell run:"
echo "  source $ROOT/ros_ws/install/setup.bash"
echo "Then:"
echo "  ros2 launch rover_bringup sim.launch.py"
