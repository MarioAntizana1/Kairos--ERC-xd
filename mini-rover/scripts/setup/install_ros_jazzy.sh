#!/usr/bin/env bash
# Install ROS 2 Jazzy and the navigation stack on Ubuntu 24.04.
#
# This script is intentionally conservative: it refuses to run on other
# operating systems and supports --dry-run so the commands can be reviewed
# before execution. It does not install hardware drivers.
set -euo pipefail

DRY_RUN=false
ASSUME_YES=false

usage() {
  cat <<'EOF'
Usage: scripts/setup/install_ros_jazzy.sh [--dry-run] [--yes]

  --dry-run   Print the commands without executing them.
  --yes, -y   Do not ask for confirmation.
  -h, --help  Show this help.

Supported platform: Ubuntu 24.04 LTS (amd64 or arm64).
EOF
}

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    --yes|-y) ASSUME_YES=true ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $arg" >&2; usage; exit 2 ;;
  esac
done

log() {
  printf '\n[%s] %s\n' "$(date +%H:%M:%S)" "$*"
}

run() {
  if [ "$DRY_RUN" = true ]; then
    printf '  '
    printf '%q ' "$@"
    printf '\n'
  else
    "$@"
  fi
}

if [ "$EUID" -eq 0 ]; then
  echo "ERROR: do not run this script as root. Run it as a normal user with sudo access." >&2
  exit 1
fi

if [ ! -r /etc/os-release ]; then
  echo "ERROR: /etc/os-release not found. Unsupported system." >&2
  exit 1
fi
# shellcheck disable=SC1091
. /etc/os-release

if [ "${ID:-}" != "ubuntu" ] || [ "${VERSION_ID:-}" != "24.04" ]; then
  cat >&2 <<EOF
ERROR: this project targets Ubuntu 24.04 LTS (Noble Numbat).
Detected: ${NAME:-unknown} ${VERSION_ID:-unknown}

ROS 2 Jazzy binary packages are built for Ubuntu 24.04. Options:
  1. Create an Ubuntu 24.04 VM (recommended).
  2. Use an Ubuntu 24.04 container (Gazebo needs GPU/X11 passthrough).
  3. Install Ubuntu 24.04 on the Raspberry Pi 4 8 GB.

See docs/05-implementacion/entorno-desarrollo.md
EOF
  exit 1
fi

case "$(uname -m)" in
  x86_64|aarch64) ;;
  *)
    echo "ERROR: unsupported architecture: $(uname -m). Use amd64 or arm64." >&2
    exit 1
    ;;
esac

UBUNTU_CODENAME="${UBUNTU_CODENAME:-noble}"
if [ "$UBUNTU_CODENAME" != "noble" ]; then
  echo "ERROR: unexpected Ubuntu codename: $UBUNTU_CODENAME" >&2
  exit 1
fi

if [ "$ASSUME_YES" = false ] && [ "$DRY_RUN" = false ]; then
  echo "This will install ROS 2 Jazzy, Nav2, Gazebo (ros_gz) and development tools."
  read -r -p "Continue? [y/N] " reply
  case "$reply" in
    y|Y|yes|YES) ;;
    *) echo "Aborted."; exit 0 ;;
  esac
fi

log "Updating apt and installing base tools"
run sudo apt update
run sudo apt install -y locales software-properties-common curl

log "Configuring UTF-8 locale"
run sudo locale-gen en_US en_US.UTF-8
run sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

log "Enabling universe repository"
run sudo add-apt-repository -y universe

log "Adding the official ROS 2 apt source"
if [ "$DRY_RUN" = true ]; then
  ROS_APT_SOURCE_VERSION="<latest>"
else
  ROS_APT_SOURCE_VERSION="$(curl -fsSL https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest \
    | sed -n 's/.*"tag_name": *"\([^"]*\)".*/\1/p' | head -n 1)"
fi
if [ -z "${ROS_APT_SOURCE_VERSION:-}" ]; then
  echo "ERROR: could not determine the latest ros2-apt-source version." >&2
  echo "Check your network or follow https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html" >&2
  exit 1
fi
APT_SOURCE_DEB="/tmp/ros2-apt-source.deb"
APT_SOURCE_URL="https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.${UBUNTU_CODENAME}_all.deb"
run curl -fL -o "$APT_SOURCE_DEB" "$APT_SOURCE_URL"
run sudo dpkg -i "$APT_SOURCE_DEB"

log "Installing ROS 2 development tools"
run sudo apt update
run sudo apt install -y ros-dev-tools

log "Installing ROS 2 Jazzy base and navigation packages"
run sudo apt install -y \
  ros-jazzy-ros-base \
  ros-jazzy-navigation2 \
  ros-jazzy-nav2-bringup \
  ros-jazzy-slam-toolbox \
  ros-jazzy-robot-localization \
  ros-jazzy-ros-gz \
  ros-jazzy-xacro \
  ros-jazzy-rviz2 \
  ros-jazzy-tf2-tools \
  ros-jazzy-teleop-twist-keyboard

log "Initializing rosdep"
if [ "$DRY_RUN" = true ] || [ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then
  run sudo rosdep init
fi
run rosdep update

log "Adding the ROS 2 setup to ~/.bashrc (if missing)"
if ! grep -qF 'source /opt/ros/jazzy/setup.bash' "$HOME/.bashrc" 2>/dev/null; then
  if [ "$DRY_RUN" = true ]; then
    printf "  echo 'source /opt/ros/jazzy/setup.bash' >> ~/.bashrc\n"
  else
    {
      echo ''
      echo '# ROS 2 Jazzy'
      echo 'source /opt/ros/jazzy/setup.bash'
    } >> "$HOME/.bashrc"
  fi
fi

if [ "$DRY_RUN" = false ]; then
  log "Verifying the installation"
  # shellcheck disable=SC1091
  source /opt/ros/jazzy/setup.bash
  ros2 doctor --report | head -n 20 || true
  if command -v gz >/dev/null 2>&1; then
    gz sim --versions || true
  fi
fi

log "Done"
cat <<'EOF'
Next steps:
  1. Open a new shell (or source /opt/ros/jazzy/setup.bash).
  2. cd <repo>/ros_ws
  3. rosdep install --from-paths src --ignore-src -r -y
  4. colcon build --symlink-install
  5. source install/setup.bash
  6. ros2 launch rover_bringup sim.launch.py

If you are on a Raspberry Pi, run `scripts/check_env.sh --strict` first.
EOF
