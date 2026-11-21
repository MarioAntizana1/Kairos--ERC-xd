"""Unit tests for the pure mission logic.

Run with:
    python3 -m unittest discover -s ros_ws/src/rover_mission/test -v
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from rover_mission.mission_planner import MissionPlanner, MissionState, Waypoint
from rover_mission.waypoints import load_mission

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DEMO_YAML = PACKAGE_ROOT / "config" / "waypoints_demo.yaml"


def wp(wp_id: str = "WP-01", x: float = 0.0, y: float = 0.0, **kwargs) -> Waypoint:
    return Waypoint(id=wp_id, x=x, y=y, **kwargs)


class WaypointValidationTests(unittest.TestCase):
    def test_valid_waypoint_uses_defaults(self) -> None:
        waypoint = wp()
        waypoint.validate()
        self.assertEqual(waypoint.yaw, 0.0)
        self.assertEqual(waypoint.tolerance, 0.25)
        self.assertEqual(waypoint.timeout_s, 90.0)

    def test_empty_id_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            wp(wp_id="   ").validate()

    def test_non_finite_coordinates_are_rejected(self) -> None:
        for value in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    wp(x=value).validate()

    def test_boolean_coordinate_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            wp(x=True).validate()  # type: ignore[arg-type]

    def test_non_positive_tolerance_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            wp(tolerance=0.0).validate()

    def test_non_positive_timeout_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            wp(timeout_s=-1.0).validate()

    def test_from_dict_requires_x_and_y(self) -> None:
        with self.assertRaises(ValueError):
            Waypoint.from_dict({"id": "A"})

    def test_from_dict_parses_numbers_and_defaults(self) -> None:
        waypoint = Waypoint.from_dict({"id": "A", "x": 1, "y": 2})
        self.assertEqual(waypoint.x, 1.0)
        self.assertEqual(waypoint.y, 2.0)
        self.assertEqual(waypoint.yaw, 0.0)


class MissionPlannerValidationTests(unittest.TestCase):
    def test_empty_mission_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MissionPlanner([])

    def test_duplicate_ids_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MissionPlanner([wp("A"), wp("A", x=1.0)])

    def test_negative_retries_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MissionPlanner([wp()], max_retries=-1)

    def test_non_integer_retries_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MissionPlanner([wp()], max_retries=1.5)  # type: ignore[arg-type]

    def test_return_to_base_requires_base(self) -> None:
        with self.assertRaises(ValueError):
            MissionPlanner([wp()], return_to_base=True)

    def test_return_to_base_accepts_base(self) -> None:
        planner = MissionPlanner([wp("BASE")], return_to_base=True)
        self.assertTrue(planner.return_to_base)

    def test_return_to_base_requires_base_last(self) -> None:
        with self.assertRaises(ValueError):
            MissionPlanner([wp("BASE"), wp("A", x=1.0)], return_to_base=True)


class MissionPlannerStateTests(unittest.TestCase):
    def test_start_only_from_idle(self) -> None:
        planner = MissionPlanner([wp()])
        self.assertEqual(planner.start(), MissionState.RUNNING)
        with self.assertRaises(RuntimeError):
            planner.start()

    def test_cannot_advance_before_start(self) -> None:
        planner = MissionPlanner([wp()])
        with self.assertRaises(RuntimeError):
            planner.mark_reached()

    def test_mark_reached_advances_to_next_waypoint(self) -> None:
        planner = MissionPlanner([wp("A"), wp("B", x=1.0)])
        planner.start()
        state = planner.mark_reached()
        self.assertEqual(state, MissionState.RUNNING)
        self.assertEqual(planner.current_waypoint.id, "B")  # type: ignore[union-attr]
        self.assertAlmostEqual(planner.progress, 0.5)

    def test_completion_sets_terminal_state(self) -> None:
        planner = MissionPlanner([wp("A")])
        planner.start()
        state = planner.mark_reached()
        self.assertEqual(state, MissionState.COMPLETED)
        self.assertTrue(planner.state.is_terminal)
        self.assertIsNone(planner.current_waypoint)
        self.assertAlmostEqual(planner.progress, 1.0)

    def test_pause_keeps_position_and_resume_continues(self) -> None:
        planner = MissionPlanner([wp("A"), wp("B", x=1.0)])
        planner.start()
        planner.pause()
        self.assertEqual(planner.state, MissionState.PAUSED)
        planner.mark_reached()
        self.assertEqual(planner.state, MissionState.PAUSED)
        self.assertEqual(planner.current_waypoint.id, "B")  # type: ignore[union-attr]
        self.assertEqual(planner.resume(), MissionState.RUNNING)

    def test_retry_then_failure(self) -> None:
        planner = MissionPlanner([wp("A")], max_retries=1)
        planner.start()
        self.assertTrue(planner.mark_failed("timeout"))
        self.assertEqual(planner.state, MissionState.RUNNING)
        self.assertEqual(planner.attempts, 1)
        self.assertFalse(planner.mark_failed("timeout"))
        self.assertEqual(planner.state, MissionState.FAILED)
        self.assertEqual(planner.failed, ("A",))

    def test_no_retries_fails_immediately(self) -> None:
        planner = MissionPlanner([wp("A")], max_retries=0)
        planner.start()
        self.assertFalse(planner.mark_failed("blocked"))
        self.assertEqual(planner.state, MissionState.FAILED)

    def test_abort_and_resume(self) -> None:
        planner = MissionPlanner([wp("A")])
        planner.start()
        self.assertTrue(planner.abort("operator abort"))
        self.assertEqual(planner.state, MissionState.ABORTED)
        self.assertEqual(planner.abort_reason, "operator abort")
        self.assertEqual(planner.resume(), MissionState.RUNNING)

    def test_abort_is_idempotent_from_terminal_state(self) -> None:
        planner = MissionPlanner([wp("A")])
        planner.start()
        planner.abort()
        self.assertFalse(planner.abort())

    def test_battery_low_is_terminal_and_cannot_resume(self) -> None:
        planner = MissionPlanner([wp("A")])
        planner.start()
        self.assertTrue(planner.mark_battery_low())
        self.assertEqual(planner.state, MissionState.BATTERY_LOW)
        with self.assertRaises(RuntimeError):
            planner.resume()

    def test_complete_with_warning(self) -> None:
        planner = MissionPlanner([wp("A")])
        planner.start()
        planner.mark_reached()
        self.assertTrue(planner.complete_with_warning("return failed"))
        self.assertEqual(planner.state, MissionState.COMPLETED_WITH_WARNING)

    def test_loop_restarts_after_last_waypoint(self) -> None:
        planner = MissionPlanner([wp("A")], loop=True)
        planner.start()
        state = planner.mark_reached()
        self.assertEqual(state, MissionState.RUNNING)
        self.assertEqual(planner.index, 0)
        self.assertAlmostEqual(planner.progress, 1.0)

    def test_summary_contains_progress_and_lists(self) -> None:
        planner = MissionPlanner([wp("A"), wp("B", x=1.0)])
        planner.start()
        planner.mark_reached()
        summary = planner.summary()
        self.assertEqual(summary["state"], "RUNNING")
        self.assertEqual(summary["reached"], ["A"])
        self.assertEqual(summary["total_waypoints"], 2)
        self.assertAlmostEqual(summary["progress"], 0.5)


class MissionFileTests(unittest.TestCase):
    def test_demo_yaml_is_valid(self) -> None:
        planner, frame_id = load_mission(DEMO_YAML)
        self.assertEqual(frame_id, "map")
        self.assertEqual(len(planner.waypoints), 5)
        self.assertEqual(planner.waypoints[-1].id, "BASE")
        self.assertTrue(planner.return_to_base)
        self.assertEqual(planner.max_retries, 1)

    def test_missing_file_raises(self) -> None:
        with self.assertRaises(ValueError):
            load_mission(PACKAGE_ROOT / "config" / "does-not-exist.yaml")

    def test_empty_waypoint_list_raises(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as handle:
            handle.write("frame_id: map\nwaypoints: []\n")
            path = Path(handle.name)
        try:
            with self.assertRaises(ValueError):
                load_mission(path)
        finally:
            path.unlink(missing_ok=True)

    def test_duplicate_waypoints_in_yaml_raise(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as handle:
            handle.write(
                "frame_id: map\n"
                "waypoints:\n"
                "  - {id: A, x: 0.0, y: 0.0}\n"
                "  - {id: A, x: 1.0, y: 1.0}\n"
            )
            path = Path(handle.name)
        try:
            with self.assertRaises(ValueError):
                load_mission(path)
        finally:
            path.unlink(missing_ok=True)

    def test_yaml_return_to_base_must_be_last(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as handle:
            handle.write(
                "frame_id: map\n"
                "return_to_base: true\n"
                "waypoints:\n"
                "  - {id: BASE, x: 0.0, y: 0.0}\n"
                "  - {id: A, x: 1.0, y: 1.0}\n"
            )
            path = Path(handle.name)
        try:
            with self.assertRaises(ValueError):
                load_mission(path)
        finally:
            path.unlink(missing_ok=True)

    def test_malformed_yaml_raises(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as handle:
            handle.write("frame_id: [\n")
            path = Path(handle.name)
        try:
            with self.assertRaises(ValueError):
                load_mission(path)
        finally:
            path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
