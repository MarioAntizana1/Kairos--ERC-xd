#!/usr/bin/env bash
# Report the host environment and whether the ROS 2 toolchain is available.
set -u

STRICT=false
if [ "${1:-}" = "--strict" ]; then
  STRICT=true
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FAILED=0

section() {
  printf '\n== %s ==\n' "$1"
}

check() {
  local name="$1"
  local command_name="$2"
  if command -v "$command_name" >/dev/null 2>&1; then
    printf '  %-12s OK  (%s)\n' "$name" "$(command -v "$command_name")"
  else
    printf '  %-12s MISSING\n' "$name"
    if [ "$STRICT" = true ]; then
      FAILED=1
    fi
  fi
}

section "Sistema"
if [ -r /etc/os-release ]; then
  # shellcheck disable=SC1091
  . /etc/os-release
  printf '  OS           %s %s\n' "${NAME:-?}" "${VERSION_ID:-?}"
else
  printf '  OS           unknown\n'
fi
printf '  Kernel       %s\n' "$(uname -r)"
printf '  Arch         %s\n' "$(uname -m)"
printf '  Hostname     %s\n' "$(hostname)"
printf '  Python       %s\n' "$(python3 --version 2>&1)"

section "Herramientas"
check "ROS 2" ros2
check "colcon" colcon
check "Gazebo" gz
check "rosdep" rosdep
check "git" git
check "make" make
check "python3" python3

section "Variables ROS"
printf '  ROS_DISTRO       %s\n' "${ROS_DISTRO:-<unset>}"
printf '  ROS_DOMAIN_ID    %s\n' "${ROS_DOMAIN_ID:-<unset>}"
printf '  ROS_LOCALHOST_ONLY %s\n' "${ROS_LOCALHOST_ONLY:-<unset>}"

section "Recursos"
printf '  CPUs         %s\n' "$(nproc)"
if command -v free >/dev/null 2>&1; then
  free -h | awk 'NR==1 || NR==2 {print "  " $0}'
fi
df -h "$ROOT" | awk 'NR==1 || NR==2 {print "  " $0}'

section "Recomendación"
if command -v ros2 >/dev/null 2>&1; then
  printf '  ROS 2 detected. Continue with: bash scripts/sim/build.sh\n'
elif [ "${ID:-}" = "ubuntu" ] && [ "${VERSION_ID:-}" = "24.04" ]; then
  printf '  Ubuntu 24.04 without ROS 2. Run: bash scripts/setup/install_ros_jazzy.sh --dry-run\n'
else
  printf '  ROS 2 Jazzy requires Ubuntu 24.04. Use a VM or container.\n'
  printf '  See docs/05-implementacion/entorno-desarrollo.md\n'
fi

if [ "$STRICT" = true ] && [ "$FAILED" -ne 0 ]; then
  exit 1
fi
exit 0
