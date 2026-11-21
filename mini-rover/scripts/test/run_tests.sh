#!/usr/bin/env bash
# Run the pure-Python mission tests and, when available, ROS integration tests.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

export PYTHONPATH="$ROOT/ros_ws/src/rover_mission${PYTHONPATH:+:$PYTHONPATH}"

echo "== Unit tests (no ROS required) =="
python3 -m unittest discover \
  -s "$ROOT/ros_ws/src/rover_mission/test" \
  -p 'test_*.py' \
  -v

if command -v ros2 >/dev/null 2>&1; then
  echo
  echo "== ROS 2 detected =="
  if [ -f "$ROOT/ros_ws/install/setup.bash" ]; then
    # shellcheck disable=SC1091
    source "/opt/ros/${ROS_DISTRO:-jazzy}/setup.bash"
    # shellcheck disable=SC1091
    source "$ROOT/ros_ws/install/setup.bash"
    echo "Integration test suites are documented in docs/06-pruebas/."
    echo "Run: ros2 launch rover_bringup sim.launch.py"
  else
    echo "Workspace not built yet; skipping ROS test discovery."
    echo "Run: bash scripts/sim/build.sh"
  fi
else
  echo
  echo "ROS 2 not found: integration and hardware tests were not run."
fi
