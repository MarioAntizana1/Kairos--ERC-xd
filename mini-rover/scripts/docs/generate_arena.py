#!/usr/bin/env python3
"""Generate the Gazebo world and the Nav2 map from a single arena description.

The arena JSON is the source of truth. Both the SDF world and the occupancy
grid are derived from it, which guarantees that the map matches the simulated
environment. The generator is deterministic: running it twice produces the
same bytes.

Usage:
    python3 scripts/docs/generate_arena.py --all
    python3 scripts/docs/generate_arena.py --check
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
ARENA_JSON = ROOT / "ros_ws/src/rover_bringup/config/arena.json"
WORLD_SDF = ROOT / "ros_ws/src/rover_bringup/worlds/mini_marsyard.sdf"
MAP_PGM = ROOT / "ros_ws/src/rover_bringup/maps/mini_marsyard.pgm"
MAP_YAML = ROOT / "ros_ws/src/rover_bringup/maps/mini_marsyard.yaml"
WAYPOINTS_YAML = ROOT / "ros_ws/src/rover_mission/config/waypoints_demo.yaml"

ROBOT_CLEARANCE_M = 0.35
FREE = 254
OCCUPIED = 0


class ArenaError(ValueError):
    """Raised when the arena description is not usable."""


def load_arena(path: Path = ARENA_JSON) -> dict[str, Any]:
    if not path.exists():
        raise ArenaError(f"arena file not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ArenaError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ArenaError("arena JSON must be an object")
    return data


def _positive(value: Any, name: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ArenaError(f"{name} must be a number") from exc
    if not math.isfinite(number) or number <= 0:
        raise ArenaError(f"{name} must be a positive finite number")
    return number


def validate_arena(cfg: dict[str, Any]) -> None:
    name = cfg.get("name")
    if not isinstance(name, str) or not name.replace("_", "").isalnum():
        raise ArenaError("name must be a non-empty alphanumeric/underscore string")

    width = _positive(cfg.get("width"), "width")
    arena_height = _positive(cfg.get("height"), "height")
    wall_thickness = _positive(cfg.get("wall_thickness"), "wall_thickness")
    _positive(cfg.get("wall_height"), "wall_height")
    resolution = _positive(cfg.get("resolution"), "resolution")
    margin = _positive(cfg.get("margin"), "margin")

    if wall_thickness >= min(width, arena_height) / 2:
        raise ArenaError("wall_thickness is too large for the arena")
    if resolution > 0.2:
        raise ArenaError("resolution must be <= 0.2 m/px")
    if margin < resolution:
        raise ArenaError("margin must be at least one pixel")

    obstacles = cfg.get("obstacles", [])
    if not isinstance(obstacles, list):
        raise ArenaError("obstacles must be a list")

    seen: set[str] = set()
    for index, obstacle in enumerate(obstacles):
        if not isinstance(obstacle, dict):
            raise ArenaError(f"obstacle[{index}] must be an object")
        obstacle_name = obstacle.get("name")
        if not isinstance(obstacle_name, str) or not obstacle_name.replace("_", "").isalnum():
            raise ArenaError(f"obstacle[{index}] has an invalid name")
        if obstacle_name in seen:
            raise ArenaError(f"duplicate obstacle name: {obstacle_name}")
        seen.add(obstacle_name)

        x = float(obstacle.get("x", 0.0))
        y = float(obstacle.get("y", 0.0))
        obstacle_height = _positive(obstacle.get("height"), f"{obstacle_name}.height")
        if not (math.isfinite(x) and math.isfinite(y)):
            raise ArenaError(f"{obstacle_name} has non-finite coordinates")

        kind = obstacle.get("type")
        if kind == "box":
            sx = _positive(obstacle.get("sx"), f"{obstacle_name}.sx")
            sy = _positive(obstacle.get("sy"), f"{obstacle_name}.sy")
            if abs(x) + sx / 2 > width / 2 or abs(y) + sy / 2 > arena_height / 2:
                raise ArenaError(f"{obstacle_name} does not fit inside the arena")
        elif kind == "cylinder":
            radius = _positive(obstacle.get("radius"), f"{obstacle_name}.radius")
            if abs(x) + radius > width / 2 or abs(y) + radius > arena_height / 2:
                raise ArenaError(f"{obstacle_name} does not fit inside the arena")
        else:
            raise ArenaError(f"{obstacle_name}.type must be 'box' or 'cylinder'")

        if obstacle_height > 2.0:
            raise ArenaError(f"{obstacle_name}.height is unreasonably large")


def _fmt(value: float) -> str:
    return f"{value:.3f}".rstrip("0").rstrip(".")


def _box_model(name: str, x: float, y: float, z: float, sx: float, sy: float, sz: float,
               color: tuple[float, float, float]) -> str:
    r, g, b = color
    return f"""    <model name="{name}">
      <static>true</static>
      <pose>{_fmt(x)} {_fmt(y)} {_fmt(z)} 0 0 0</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <box>
              <size>{_fmt(sx)} {_fmt(sy)} {_fmt(sz)}</size>
            </box>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>1.0</mu>
                <mu2>1.0</mu2>
              </ode>
            </friction>
          </surface>
        </collision>
        <visual name="visual">
          <geometry>
            <box>
              <size>{_fmt(sx)} {_fmt(sy)} {_fmt(sz)}</size>
            </box>
          </geometry>
          <material>
            <ambient>{_fmt(r)} {_fmt(g)} {_fmt(b)} 1</ambient>
            <diffuse>{_fmt(r)} {_fmt(g)} {_fmt(b)} 1</diffuse>
            <specular>0.05 0.05 0.05 1</specular>
          </material>
        </visual>
      </link>
    </model>"""


def _cylinder_model(name: str, x: float, y: float, z: float, radius: float, height: float,
                    color: tuple[float, float, float]) -> str:
    r, g, b = color
    return f"""    <model name="{name}">
      <static>true</static>
      <pose>{_fmt(x)} {_fmt(y)} {_fmt(z)} 0 0 0</pose>
      <link name="link">
        <collision name="collision">
          <geometry>
            <cylinder>
              <radius>{_fmt(radius)}</radius>
              <length>{_fmt(height)}</length>
            </cylinder>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>1.0</mu>
                <mu2>1.0</mu2>
              </ode>
            </friction>
          </surface>
        </collision>
        <visual name="visual">
          <geometry>
            <cylinder>
              <radius>{_fmt(radius)}</radius>
              <length>{_fmt(height)}</length>
            </cylinder>
          </geometry>
          <material>
            <ambient>{_fmt(r)} {_fmt(g)} {_fmt(b)} 1</ambient>
            <diffuse>{_fmt(r)} {_fmt(g)} {_fmt(b)} 1</diffuse>
            <specular>0.05 0.05 0.05 1</specular>
          </material>
        </visual>
      </link>
    </model>"""


def build_world(cfg: dict[str, Any]) -> str:
    width = float(cfg["width"])
    height = float(cfg["height"])
    wall_thickness = float(cfg["wall_thickness"])
    wall_height = float(cfg["wall_height"])
    name = cfg["name"]

    obstacles = []
    for obstacle in cfg.get("obstacles", []):
        if obstacle["type"] == "box":
            obstacles.append(_box_model(
                obstacle["name"],
                float(obstacle["x"]),
                float(obstacle["y"]),
                float(obstacle["height"]) / 2.0,
                float(obstacle["sx"]),
                float(obstacle["sy"]),
                float(obstacle["height"]),
                (0.42, 0.30, 0.20),
            ))
        else:
            obstacles.append(_cylinder_model(
                obstacle["name"],
                float(obstacle["x"]),
                float(obstacle["y"]),
                float(obstacle["height"]) / 2.0,
                float(obstacle["radius"]),
                float(obstacle["height"]),
                (0.36, 0.26, 0.18),
            ))

    walls = [
        _box_model("wall_north", 0.0, height / 2 + wall_thickness / 2, wall_height / 2,
                   width + 2 * wall_thickness, wall_thickness, wall_height, (0.30, 0.30, 0.32)),
        _box_model("wall_south", 0.0, -height / 2 - wall_thickness / 2, wall_height / 2,
                   width + 2 * wall_thickness, wall_thickness, wall_height, (0.30, 0.30, 0.32)),
        _box_model("wall_east", width / 2 + wall_thickness / 2, 0.0, wall_height / 2,
                   wall_thickness, height, wall_height, (0.30, 0.30, 0.32)),
        _box_model("wall_west", -width / 2 - wall_thickness / 2, 0.0, wall_height / 2,
                   wall_thickness, height, wall_height, (0.30, 0.30, 0.32)),
    ]

    body = "\n".join(walls + obstacles)
    return f"""<?xml version="1.0" ?>
<!-- Generated by scripts/docs/generate_arena.py from config/arena.json. Do not edit. -->
<sdf version="1.9">
  <world name="{name}">
    <gravity>0 0 -9.81</gravity>
    <physics name="1ms" type="ignored">
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1.0</real_time_factor>
    </physics>

    <plugin filename="gz-sim-physics-system" name="gz::sim::systems::Physics"/>
    <plugin filename="gz-sim-user-commands-system" name="gz::sim::systems::UserCommands"/>
    <plugin filename="gz-sim-scene-broadcaster-system" name="gz::sim::systems::SceneBroadcaster"/>
    <plugin filename="gz-sim-sensors-system" name="gz::sim::systems::Sensors">
      <render_engine>ogre2</render_engine>
    </plugin>
    <plugin filename="gz-sim-imu-system" name="gz::sim::systems::Imu"/>

    <scene>
      <ambient>0.45 0.42 0.40 1</ambient>
      <background>0.20 0.16 0.14 1</background>
      <shadows>true</shadows>
    </scene>

    <light type="directional" name="sun">
      <cast_shadows>true</cast_shadows>
      <pose>0 0 10 0 0 0</pose>
      <diffuse>0.85 0.82 0.75 1</diffuse>
      <specular>0.20 0.20 0.20 1</specular>
      <direction>-0.5 0.5 -1</direction>
    </light>

    <model name="ground_plane">
      <static>true</static>
      <link name="link">
        <collision name="collision">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>0.8</mu>
                <mu2>0.8</mu2>
              </ode>
            </friction>
          </surface>
        </collision>
        <visual name="visual">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <ambient>0.34 0.22 0.16 1</ambient>
            <diffuse>0.45 0.30 0.20 1</diffuse>
            <specular>0.05 0.05 0.05 1</specular>
          </material>
        </visual>
      </link>
    </model>

{body}
  </world>
</sdf>
"""


def build_map(cfg: dict[str, Any]) -> tuple[bytes, str]:
    width = float(cfg["width"])
    height = float(cfg["height"])
    resolution = float(cfg["resolution"])
    margin = float(cfg["margin"])
    name = cfg["name"]

    cols = int(round((width + 2 * margin) / resolution))
    rows = int(round((height + 2 * margin) / resolution))
    origin_x = -width / 2 - margin
    origin_y = -height / 2 - margin

    pixels = bytearray([OCCUPIED]) * (cols * rows)

    # Free space is the arena interior; the border represents the walls and
    # everything outside them.
    for row in range(rows):
        y = origin_y + (rows - 1 - row + 0.5) * resolution
        if abs(y) > height / 2:
            continue
        for col in range(cols):
            x = origin_x + (col + 0.5) * resolution
            if abs(x) <= width / 2:
                pixels[row * cols + col] = FREE

    def mark_box(obstacle: dict[str, Any]) -> None:
        ox = float(obstacle["x"])
        oy = float(obstacle["y"])
        sx = float(obstacle["sx"])
        sy = float(obstacle["sy"])
        col_min = max(0, int(math.floor((ox - sx / 2 - origin_x) / resolution)))
        col_max = min(cols - 1, int(math.ceil((ox + sx / 2 - origin_x) / resolution)))
        row_min = max(0, int(math.floor((oy - sy / 2 - origin_y) / resolution)))
        row_max = min(rows - 1, int(math.ceil((oy + sy / 2 - origin_y) / resolution)))
        for row in range(row_min, row_max + 1):
            y = origin_y + (row + 0.5) * resolution
            if abs(y - oy) > sy / 2:
                continue
            for col in range(col_min, col_max + 1):
                x = origin_x + (col + 0.5) * resolution
                if abs(x - ox) <= sx / 2:
                    pixels[(rows - 1 - row) * cols + col] = OCCUPIED

    def mark_cylinder(obstacle: dict[str, Any]) -> None:
        ox = float(obstacle["x"])
        oy = float(obstacle["y"])
        radius = float(obstacle["radius"])
        col_min = max(0, int(math.floor((ox - radius - origin_x) / resolution)))
        col_max = min(cols - 1, int(math.ceil((ox + radius - origin_x) / resolution)))
        row_min = max(0, int(math.floor((oy - radius - origin_y) / resolution)))
        row_max = min(rows - 1, int(math.ceil((oy + radius - origin_y) / resolution)))
        for row in range(row_min, row_max + 1):
            y = origin_y + (row + 0.5) * resolution
            for col in range(col_min, col_max + 1):
                x = origin_x + (col + 0.5) * resolution
                if (x - ox) ** 2 + (y - oy) ** 2 <= radius ** 2:
                    pixels[(rows - 1 - row) * cols + col] = OCCUPIED

    for obstacle in cfg.get("obstacles", []):
        if obstacle["type"] == "box":
            mark_box(obstacle)
        else:
            mark_cylinder(obstacle)

    header = f"P5\n{cols} {rows}\n255\n".encode("ascii")
    pgm = header + bytes(pixels)

    map_yaml = (
        f"image: {name}.pgm\n"
        f"resolution: {resolution}\n"
        f"origin: [{origin_x}, {origin_y}, 0.0]\n"
        "negate: 0\n"
        "occupied_thresh: 0.65\n"
        "free_thresh: 0.196\n"
        "mode: trinary\n"
    )
    return pgm, map_yaml


def _map_geometry(cfg: dict[str, Any]) -> tuple[int, int, float, float, bytes]:
    pgm, _ = build_map(cfg)
    header_end = pgm.index(b"\n255\n") + len(b"\n255\n")
    header = pgm[:header_end].decode("ascii").splitlines()
    cols, rows = (int(v) for v in header[1].split())
    margin = float(cfg["margin"])
    origin_x = -float(cfg["width"]) / 2 - margin
    origin_y = -float(cfg["height"]) / 2 - margin
    return cols, rows, origin_x, origin_y, pgm[header_end:]


def validate_waypoints(cfg: dict[str, Any], path: Path = WAYPOINTS_YAML) -> list[str]:
    if not path.exists():
        return [f"waypoints file not found: {path}"]
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [f"invalid YAML in {path}: {exc}"]

    if not isinstance(data, dict):
        return ["waypoints YAML must be an object"]
    waypoints = data.get("waypoints")
    if not isinstance(waypoints, list) or not waypoints:
        return ["waypoints must be a non-empty list"]

    cols, rows, origin_x, origin_y, pixels = _map_geometry(cfg)
    resolution = float(cfg["resolution"])
    errors: list[str] = []
    seen: set[str] = set()

    for index, waypoint in enumerate(waypoints):
        if not isinstance(waypoint, dict):
            errors.append(f"waypoint[{index}] must be an object")
            continue
        wp_id = waypoint.get("id")
        if not isinstance(wp_id, str) or not wp_id:
            errors.append(f"waypoint[{index}] has no id")
            continue
        if wp_id in seen:
            errors.append(f"duplicate waypoint id: {wp_id}")
        seen.add(wp_id)

        try:
            x = float(waypoint["x"])
            y = float(waypoint["y"])
        except (KeyError, TypeError, ValueError):
            errors.append(f"{wp_id} has invalid x/y")
            continue
        if not (math.isfinite(x) and math.isfinite(y)):
            errors.append(f"{wp_id} has non-finite coordinates")
            continue

        col = int(math.floor((x - origin_x) / resolution))
        row_from_bottom = int(math.floor((y - origin_y) / resolution))
        row = rows - 1 - row_from_bottom
        if not (0 <= col < cols and 0 <= row < rows):
            errors.append(f"{wp_id} is outside the map")
            continue

        radius_cells = int(math.ceil(ROBOT_CLEARANCE_M / resolution))
        blocked = False
        for dr in range(-radius_cells, radius_cells + 1):
            for dc in range(-radius_cells, radius_cells + 1):
                if dc * dc + dr * dr > radius_cells * radius_cells:
                    continue
                rr = row + dr
                cc = col + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    if pixels[rr * cols + cc] == OCCUPIED:
                        blocked = True
                        break
            if blocked:
                break
        if blocked:
            errors.append(
                f"{wp_id} at ({x}, {y}) is not free with {ROBOT_CLEARANCE_M} m clearance"
            )

    if data.get("return_to_base") and "BASE" not in seen:
        errors.append("return_to_base is true but no BASE waypoint exists")

    return errors


def _write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _read(path: Path) -> bytes:
    return path.read_bytes()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--all", action="store_true", help="write world, map and YAML")
    group.add_argument("--check", action="store_true", help="verify generated assets are current")
    args = parser.parse_args(argv)

    try:
        cfg = load_arena()
        validate_arena(cfg)
        world = build_world(cfg).encode("utf-8")
        pgm, map_yaml = build_map(cfg)
        waypoint_errors = validate_waypoints(cfg)
    except ArenaError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if waypoint_errors:
        print("ERROR: waypoint validation failed:", file=sys.stderr)
        for error in waypoint_errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    if args.check:
        problems: list[str] = []
        if not WORLD_SDF.exists():
            problems.append(f"missing {WORLD_SDF.relative_to(ROOT)}")
        elif _read(WORLD_SDF) != world:
            problems.append(f"outdated {WORLD_SDF.relative_to(ROOT)}")
        if not MAP_PGM.exists():
            problems.append(f"missing {MAP_PGM.relative_to(ROOT)}")
        elif _read(MAP_PGM) != pgm:
            problems.append(f"outdated {MAP_PGM.relative_to(ROOT)}")
        if not MAP_YAML.exists():
            problems.append(f"missing {MAP_YAML.relative_to(ROOT)}")
        elif _read(MAP_YAML) != map_yaml.encode("utf-8"):
            problems.append(f"outdated {MAP_YAML.relative_to(ROOT)}")

        if problems:
            print("ERROR: generated assets are not up to date:", file=sys.stderr)
            for problem in problems:
                print(f"  - {problem}", file=sys.stderr)
            print("Run: python3 scripts/docs/generate_arena.py --all", file=sys.stderr)
            return 1

        cols, rows, origin_x, origin_y, _ = _map_geometry(cfg)
        print(
            f"OK: {cfg['name']} — map {cols}x{rows} px, "
            f"origin ({origin_x}, {origin_y}), waypoints validated"
        )
        return 0

    _write(WORLD_SDF, world)
    _write(MAP_PGM, pgm)
    _write(MAP_YAML, map_yaml.encode("utf-8"))
    cols, rows, origin_x, origin_y, _ = _map_geometry(cfg)
    print(f"Wrote {WORLD_SDF.relative_to(ROOT)}")
    print(f"Wrote {MAP_PGM.relative_to(ROOT)}")
    print(f"Wrote {MAP_YAML.relative_to(ROOT)}")
    print(
        f"Map: {cols}x{rows} px, {cfg['resolution']} m/px, "
        f"origin ({origin_x}, {origin_y})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
