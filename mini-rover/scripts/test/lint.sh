#!/usr/bin/env bash
# Syntax and hygiene checks that work on any Linux host.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

python3 scripts/test/check_syntax.py

if command -v ruff >/dev/null 2>&1; then
  echo
  echo "== ruff (undefined names and syntax errors) =="
  ruff check --select E9,F --output-format concise .
else
  echo
  echo "ruff not installed: skipped (optional; pip install ruff)."
fi

if command -v xacro >/dev/null 2>&1; then
  echo
  echo "== xacro/URDF =="
  tmp_urdf="$(mktemp)"
  trap 'rm -f "$tmp_urdf"' EXIT
  xacro ros_ws/src/rover_description/urdf/rover.urdf.xacro > "$tmp_urdf"
  python3 scripts/test/check_urdf.py "$tmp_urdf"
else
  echo
  echo "xacro not installed: skipped (install ros-jazzy-xacro)."
fi

if command -v shellcheck >/dev/null 2>&1; then
  echo
  echo "== shellcheck =="
  find scripts -type f -name '*.sh' -print0 | xargs -0 shellcheck
else
  echo
  echo "shellcheck not installed: skipped (install it for stricter Bash checks)."
fi

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo
  echo "== git whitespace check =="
  git diff --check
fi

echo
echo "OK: lint checks completed"
