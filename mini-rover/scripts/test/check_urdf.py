#!/usr/bin/env python3
"""Static checks for a generated URDF file (no ROS required).

Usage:
    python3 scripts/test/check_urdf.py /tmp/rover.urdf
"""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

VALID_JOINT_TYPES = {
    "fixed",
    "revolute",
    "continuous",
    "prismatic",
    "floating",
    "planar",
}


def check(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [f"invalid XML: {exc}"]

    if root.tag != "robot":
        return [f"root element must be <robot>, got <{root.tag}>"]

    links = root.findall("link")
    link_names = [link.get("name") for link in links]
    if not links:
        errors.append("no links found")
    if len(link_names) != len(set(link_names)):
        errors.append("duplicate link names")

    joints = root.findall("joint")
    if not joints:
        errors.append("no joints found")
    joint_names = [joint.get("name") for joint in joints]
    if len(joint_names) != len(set(joint_names)):
        errors.append("duplicate joint names")

    for joint in joints:
        name = joint.get("name", "<unnamed>")
        joint_type = joint.get("type")
        parent = joint.find("parent")
        child = joint.find("child")
        if parent is None or parent.get("link") is None:
            errors.append(f"joint {name}: missing parent link")
        elif parent.get("link") not in link_names:
            errors.append(f"joint {name}: parent link not found: {parent.get('link')}")
        if child is None or child.get("link") is None:
            errors.append(f"joint {name}: missing child link")
        elif child.get("link") not in link_names:
            errors.append(f"joint {name}: child link not found: {child.get('link')}")
        if joint_type not in VALID_JOINT_TYPES:
            errors.append(f"joint {name}: invalid type {joint_type!r}")
        if joint_type in {"revolute", "continuous", "prismatic"} and joint.find("axis") is None:
            errors.append(f"joint {name}: missing axis")

    for link in links:
        inertial = link.find("inertial")
        if inertial is None:
            continue
        mass = inertial.find("mass")
        if mass is None:
            errors.append(f"link {link.get('name')}: inertial without mass")
            continue
        try:
            value = float(mass.get("value", "0"))
        except ValueError:
            errors.append(f"link {link.get('name')}: invalid mass")
            continue
        if value <= 0:
            errors.append(f"link {link.get('name')}: mass must be positive")

    sensors = {sensor.get("name") for sensor in root.findall(".//sensor")}
    for required in ("lidar", "imu"):
        if required not in sensors:
            errors.append(f"missing sensor: {required}")

    plugins = {
        plugin.get("filename")
        for plugin in root.findall(".//plugin")
        if plugin.get("filename")
    }
    for required in ("gz-sim-diff-drive-system", "gz-sim-joint-state-publisher-system"):
        if required not in plugins:
            errors.append(f"missing Gazebo plugin: {required}")

    if not errors:
        print(
            f"URDF OK: {len(links)} links, {len(joints)} joints, "
            f"{len(sensors)} sensors, {len(plugins)} gazebo plugins"
        )
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python3 scripts/test/check_urdf.py <robot.urdf>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2
    errors = check(path)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"FAILED: {len(errors)} URDF error(s)", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
