#!/usr/bin/env bash
# Preflight checks before a mission. Run with --sim to skip hardware-only checks.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SIM=false
ASSUME_YES=false

usage() {
  cat <<'EOF'
Usage: scripts/demo/preflight.sh [--sim] [--yes]

  --sim   Simulation mode: skip e-stop/battery confirmations, require /clock.
  --yes   Do not ask for the e-stop confirmation (hardware mode).
EOF
}

for arg in "$@"; do
  case "$arg" in
    --sim) SIM=true ;;
    --yes|-y) ASSUME_YES=true ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $arg" >&2; usage; exit 2 ;;
  esac
done

if ! command -v ros2 >/dev/null 2>&1; then
  echo "ERROR: ROS 2 is not available. Source /opt/ros/jazzy/setup.bash." >&2
  exit 2
fi

# shellcheck disable=SC1090
source "/opt/ros/${ROS_DISTRO:-jazzy}/setup.bash"
if [ -f "$ROOT/ros_ws/install/setup.bash" ]; then
  # shellcheck disable=SC1091
  source "$ROOT/ros_ws/install/setup.bash"
fi

FAILED=0
ok() { printf '  [OK]   %s\n' "$*"; }
fail() { printf '  [FAIL] %s\n' "$*"; FAILED=1; }

echo "== Preflight =="
echo "Mode: $([ "$SIM" = true ] && echo simulation || echo hardware)"
echo

if ros2 pkg prefix rover_mission >/dev/null 2>&1; then
  ok "rover_mission package is available"
else
  fail "rover_mission package not found (build the workspace)"
fi

for topic in /scan /odom /tf /cmd_vel /rover/mission/status; do
  if ros2 topic list 2>/dev/null | grep -qx "$topic"; then
    ok "topic $topic is present"
  else
    fail "topic $topic is missing"
  fi
done

if [ "$SIM" = true ]; then
  if ros2 topic list 2>/dev/null | grep -qx "/clock"; then
    ok "topic /clock is present"
  else
    fail "topic /clock is missing (is Gazebo running?)"
  fi
fi

if ros2 action list 2>/dev/null | grep -q "navigate_to_pose"; then
  ok "navigate_to_pose action is available"
else
  fail "navigate_to_pose action is missing (is Nav2 active?)"
fi

TF_OUTPUT="$(timeout 5 ros2 run tf2_ros tf2_echo map base_footprint 2>&1 || true)"
if printf '%s' "$TF_OUTPUT" | grep -q "Translation"; then
  ok "TF map -> base_footprint is available"
else
  fail "TF map -> base_footprint is not available"
fi

AVAILABLE_KB="$(df -Pk "$ROOT" | awk 'NR==2 {print $4}')"
if [ -n "$AVAILABLE_KB" ] && [ "$AVAILABLE_KB" -gt 1048576 ]; then
  ok "disk space > 1 GB ($AVAILABLE_KB KB free)"
else
  fail "less than 1 GB free on the repository filesystem"
fi

if [ "$SIM" = false ]; then
  if [ "$ASSUME_YES" = true ]; then
    ok "e-stop confirmation skipped (--yes)"
  else
    read -r -p "  Is the physical e-stop tested and accessible? [y/N] " reply
    case "$reply" in
      y|Y|yes|YES) ok "e-stop confirmed by operator" ;;
      *) fail "e-stop not confirmed" ;;
    esac
  fi
fi

echo
if [ "$FAILED" -ne 0 ]; then
  echo "PREFLIGHT FAILED: fix the items above before moving the rover."
  exit 1
fi
echo "PREFLIGHT OK: ready to start the mission."
