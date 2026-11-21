#!/usr/bin/env bash
# Record a rosbag2 of the mission topics into an evidence folder.
#
# Usage: record_bag.sh <evidence-dir> [duration-seconds]
# If duration is omitted or 0, recording continues until Ctrl-C.
set -euo pipefail

DIR="${1:-}"
DURATION="${2:-0}"
if [ -z "$DIR" ]; then
  echo "Usage: bash scripts/evidence/record_bag.sh <evidence-dir> [duration-seconds]" >&2
  exit 2
fi
if [ ! -d "$DIR" ]; then
  echo "ERROR: not a directory: $DIR" >&2
  exit 1
fi
if ! command -v ros2 >/dev/null 2>&1; then
  echo "ERROR: ROS 2 is not available in this shell." >&2
  exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
# shellcheck disable=SC1090
source "/opt/ros/${ROS_DISTRO:-jazzy}/setup.bash"
if [ -f "$ROOT/ros_ws/install/setup.bash" ]; then
  # shellcheck disable=SC1091
  source "$ROOT/ros_ws/install/setup.bash"
fi

mkdir -p "$DIR/bags"
OUT="$DIR/bags/rosbag2_$(date +%Y%m%d_%H%M%S)"
TOPICS=(
  /tf
  /tf_static
  /scan
  /odom
  /imu
  /cmd_vel
  /rover/mission/status
  /rover/mission/progress
)

echo "Recording to: $OUT"
echo "Topics: ${TOPICS[*]}"

set +e
if [ "$DURATION" -gt 0 ] 2>/dev/null; then
  timeout --signal=INT "$DURATION" ros2 bag record -o "$OUT" "${TOPICS[@]}"
  rc=$?
else
  ros2 bag record -o "$OUT" "${TOPICS[@]}"
  rc=$?
fi
set -e

# timeout returns 124 when it stops the process; 130 is Ctrl-C.
if [ "$rc" -ne 0 ] && [ "$rc" -ne 124 ] && [ "$rc" -ne 130 ]; then
  echo "ERROR: ros2 bag record failed with code $rc" >&2
  exit "$rc"
fi

echo "Bag saved: $OUT"
