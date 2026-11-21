#!/usr/bin/env bash
# Launch the mission node against a running Nav2 stack.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

if ! command -v ros2 >/dev/null 2>&1; then
  echo "ERROR: ROS 2 is not available. Use Ubuntu 24.04 with ROS 2 Jazzy." >&2
  exit 1
fi
if [ ! -f "$ROOT/ros_ws/install/setup.bash" ]; then
  echo "ERROR: workspace not built. Run: bash scripts/sim/build.sh" >&2
  exit 1
fi

# shellcheck disable=SC1090
source "/opt/ros/${ROS_DISTRO:-jazzy}/setup.bash"
# shellcheck disable=SC1091
source "$ROOT/ros_ws/install/setup.bash"

exec ros2 launch rover_bringup mission.launch.py "$@"
