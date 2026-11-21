"""Load and validate a mission YAML file."""

from __future__ import annotations

from pathlib import Path

import yaml

from .mission_planner import MissionPlanner, Waypoint


def load_mission(
    path: str | Path,
    max_retries: int = 1,
) -> tuple[MissionPlanner, str]:
    """Load a mission file and return (planner, frame_id).

    Raises ValueError with a human-readable message when the file is missing,
    malformed or semantically invalid.
    """
    mission_path = Path(path).expanduser()
    if not mission_path.exists():
        raise ValueError(f"waypoints file not found: {mission_path}")
    if not mission_path.is_file():
        raise ValueError(f"waypoints path is not a file: {mission_path}")

    try:
        data = yaml.safe_load(mission_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML in {mission_path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("mission file must contain a YAML object")

    frame_id = data.get("frame_id", "map")
    if not isinstance(frame_id, str) or not frame_id.strip():
        raise ValueError("frame_id must be a non-empty string")

    raw_waypoints = data.get("waypoints")
    if not isinstance(raw_waypoints, list) or not raw_waypoints:
        raise ValueError("waypoints must be a non-empty list")

    waypoints: list[Waypoint] = []
    for index, raw in enumerate(raw_waypoints):
        try:
            if not isinstance(raw, dict):
                raise ValueError("waypoint must be an object")
            waypoints.append(Waypoint.from_dict(raw))
        except (TypeError, ValueError) as exc:
            raise ValueError(f"invalid waypoint at index {index}: {exc}") from exc

    retries = data.get("max_retries", max_retries)
    loop = data.get("loop", False)
    return_to_base = data.get("return_to_base", False)
    for name, value in (("loop", loop), ("return_to_base", return_to_base)):
        if not isinstance(value, bool):
            raise ValueError(f"{name} must be a boolean")

    if return_to_base and waypoints[-1].id != "BASE":
        raise ValueError("return_to_base requires 'BASE' to be the last waypoint")

    try:
        planner = MissionPlanner(
            waypoints,
            max_retries=retries,
            loop=loop,
            return_to_base=return_to_base,
        )
    except (TypeError, ValueError) as exc:
        raise ValueError(f"invalid mission: {exc}") from exc

    return planner, frame_id
