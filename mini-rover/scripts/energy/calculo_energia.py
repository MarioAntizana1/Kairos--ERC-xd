#!/usr/bin/env python3
"""Preliminary energy budget for the Rover Mini Demo.

The model is intentionally parametric: every number that is not taken from a
datasheet is an explicit assumption that must be replaced by a measurement
before the design is frozen. Run with ``--json`` for machine-readable output.

Note: the electronics defaults model the 6x6 study with a Raspberry Pi 5. The
base mini demo now uses a Raspberry Pi 4 8 GB (ADR-0010); update this model if
the 6x6 variant is adopted.

Usage:
    python3 scripts/energy/calculo_energia.py
    python3 scripts/energy/calculo_energia.py --json
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass

G = 9.81  # m/s^2
KGCM_PER_NM = 1.0 / 0.0980665  # 1 kgf.cm = 0.0980665 N.m


@dataclass(frozen=True)
class Motor:
    """Reference traction motor. NOT a final selection."""

    name: str = "Pololu 25D LP 6V 99:1 with encoder (item 4827)"
    rated_voltage_v: float = 6.0
    no_load_current_a: float = 0.12
    stall_current_a: float = 2.0
    stall_torque_kgcm: float = 9.1


@dataclass(frozen=True)
class Rover:
    """Mechanical assumptions for the reference rover."""

    mass_kg: float = 6.0
    wheels: int = 6
    wheel_radius_m: float = 0.060
    cruise_speed_mps: float = 0.30
    rolling_resistance: float = 0.08
    slope_deg: float = 10.0
    drivetrain_efficiency: float = 0.45
    driver_loss_w: float = 0.4


@dataclass(frozen=True)
class Electronics:
    """Average loads on the 5 V and 6 V rails."""

    pi5_w: float = 4.0
    nvme_w: float = 1.5
    camera_w: float = 1.25
    lidar_w: float = 0.5
    mcu_w: float = 0.5
    radio_w: float = 0.3
    fan_w: float = 0.3
    buck5_efficiency: float = 0.90

    servo_count: int = 6
    servo_voltage_v: float = 6.0
    servo_idle_a: float = 0.02
    servo_active_a: float = 0.60
    servo_duty: float = 0.10
    servo_stall_a: float = 2.5
    bec_efficiency: float = 0.85


@dataclass(frozen=True)
class Pack:
    """Li-ion 18650 pack made from 3.6 V / 3500 mAh cells."""

    name: str
    cells: int
    configuration: str
    voltage_v: float
    capacity_ah: float
    parallel_strings: int
    max_dod: float = 0.80

    @property
    def energy_wh(self) -> float:
        return self.voltage_v * self.capacity_ah

    @property
    def usable_wh(self) -> float:
        return self.energy_wh * self.max_dod


@dataclass(frozen=True)
class Solar:
    """User-supplied photovoltaic panels."""

    panels: int = 4
    vmp_v: float = 7.2
    imp_a: float = 0.60
    isc_to_imp: float = 0.80  # if 600 mA is Isc, Imp is lower
    derate: float = 0.75  # temperature, angle, dust
    charger_efficiency: float = 0.90
    peak_sun_hours: float = 3.0


PACKS = (
    Pack("2S1P", 2, "2S1P", 7.2, 3.5, 1),
    Pack("2S2P", 4, "2S2P", 7.2, 7.0, 2),
    Pack("2S3P", 6, "2S3P", 7.2, 10.5, 3),
    Pack("2S4P", 8, "2S4P", 7.2, 14.0, 4),
    Pack("2S8P", 16, "2S8P", 7.2, 28.0, 8),
)


def drive_power(rover: Rover, motor: Motor) -> dict[str, float]:
    """Electrical power for all traction motors on flat ground and on a slope."""
    weight = rover.mass_kg * G
    rolling_force = rover.rolling_resistance * weight
    slope_force = weight * math.sin(math.radians(rover.slope_deg))
    speed = rover.cruise_speed_mps

    flat_mech = rolling_force * speed
    slope_mech = (rolling_force + slope_force) * speed

    flat_traction = flat_mech / rover.drivetrain_efficiency
    slope_traction = slope_mech / rover.drivetrain_efficiency
    no_load = rover.wheels * motor.rated_voltage_v * motor.no_load_current_a

    return {
        "rolling_force_n": rolling_force,
        "slope_force_n": slope_force,
        "flat_mechanical_w": flat_mech,
        "slope_mechanical_w": slope_mech,
        "flat_traction_w": flat_traction,
        "slope_traction_w": slope_traction,
        "no_load_w": no_load,
        "flat_total_w": flat_traction + no_load + rover.driver_loss_w,
        "slope_total_w": slope_traction + no_load + rover.driver_loss_w,
    }


def electronics_power(electronics: Electronics) -> dict[str, float]:
    """Average power drawn from the battery by the 5 V and 6 V rails."""
    five_v_loads = {
        "Raspberry Pi 5 8 GB": electronics.pi5_w,
        "NVMe SSD (optional)": electronics.nvme_w,
        "Camera Module 3": electronics.camera_w,
        "2D LiDAR (optional)": electronics.lidar_w,
        "MCU / flight controller": electronics.mcu_w,
        "RC link / telemetry": electronics.radio_w,
        "Pi 5 fan": electronics.fan_w,
    }
    five_v_total = sum(five_v_loads.values())
    five_v_battery = five_v_total / electronics.buck5_efficiency

    servo_avg_a = electronics.servo_idle_a + electronics.servo_duty * (
        electronics.servo_active_a - electronics.servo_idle_a
    )
    servo_total_w = (
        electronics.servo_count * electronics.servo_voltage_v * servo_avg_a
    )
    servo_battery = servo_total_w / electronics.bec_efficiency

    return {
        "five_v_loads": five_v_loads,
        "five_v_total_w": five_v_total,
        "five_v_battery_w": five_v_battery,
        "servo_avg_a": servo_avg_a,
        "servo_total_w": servo_total_w,
        "servo_battery_w": servo_battery,
        "total_battery_w": five_v_battery + servo_battery,
    }


def mission_profiles(
    idle_w: float, cruise_w: float, slope_w: float
) -> list[dict[str, float | str]]:
    """Weighted mission profiles: cruise, slope and idle fractions."""
    definitions = (
        ("Demo 20 min", 20, 0.50, 0.15),
        ("RNF-06 30 min", 30, 0.50, 0.15),
        ("Extended 45 min", 45, 0.55, 0.10),
        ("Target 60 min", 60, 0.55, 0.10),
    )
    profiles = []
    for name, minutes, cruise_fraction, slope_fraction in definitions:
        idle_fraction = 1.0 - cruise_fraction - slope_fraction
        average_w = (
            cruise_fraction * cruise_w
            + slope_fraction * slope_w
            + idle_fraction * idle_w
        )
        profiles.append(
            {
                "name": name,
                "minutes": minutes,
                "cruise_fraction": cruise_fraction,
                "slope_fraction": slope_fraction,
                "idle_fraction": idle_fraction,
                "average_w": average_w,
                "energy_wh": average_w * minutes / 60.0,
            }
        )
    return profiles


def pack_table(
    packs: tuple[Pack, ...], average_w: float, mission_wh: float
) -> list[dict[str, float | int | str]]:
    """Runtime and per-cell current for each pack option."""
    rows = []
    for pack in packs:
        pack_current = average_w / pack.voltage_v
        rows.append(
            {
                "name": pack.name,
                "cells": pack.cells,
                "configuration": pack.configuration,
                "energy_wh": pack.energy_wh,
                "usable_wh": pack.usable_wh,
                "runtime_h": pack.usable_wh / average_w,
                "missions": pack.usable_wh / mission_wh,
                "pack_current_a": pack_current,
                "cell_current_a": pack_current / pack.parallel_strings,
            }
        )
    return rows


def solar_table(solar: Solar, cruise_w: float, mission_wh: float) -> dict[str, float]:
    """Peak and daily energy from the panels.

    Two cases are reported because the user's "600 mA" may be Imp or Isc.
    The conservative case (600 mA = Isc) is used for the verdict.
    """
    p_stc = solar.panels * solar.vmp_v * solar.imp_a
    p_if_isc = p_stc * solar.isc_to_imp
    p_effective_imp = p_stc * solar.derate * solar.charger_efficiency
    p_effective_isc = p_if_isc * solar.derate * solar.charger_efficiency
    daily_imp = p_effective_imp * solar.peak_sun_hours
    daily_isc = p_effective_isc * solar.peak_sun_hours
    return {
        "p_stc_w": p_stc,
        "p_if_isc_w": p_if_isc,
        "p_effective_imp_w": p_effective_imp,
        "p_effective_isc_w": p_effective_isc,
        "daily_imp_wh": daily_imp,
        "daily_isc_wh": daily_isc,
        "deficit_isc_w": p_effective_isc - cruise_w,
        "missions_per_day_isc": daily_isc / mission_wh,
        "charge_voltage_v": 4.2 * 2,
    }


def steering_table(
    masses: tuple[float, ...] = (4.0, 6.0, 8.0, 10.0, 12.0),
    mu: float = 0.8,
    scrub_radius_m: float = 0.030,
    safety_factor: float = 2.0,
) -> list[dict[str, float]]:
    """Static steering torque per wheel for a 6-wheel rover."""
    rows = []
    for mass in masses:
        normal_force = mass * G / 6.0
        friction_force = mu * normal_force
        torque_nm = friction_force * scrub_radius_m * safety_factor
        rows.append(
            {
                "mass_kg": mass,
                "normal_force_n": normal_force,
                "torque_nm": torque_nm,
                "torque_kgcm": torque_nm * KGCM_PER_NM,
            }
        )
    return rows


def peak_power(
    rover: Rover, motor: Motor, electronics: Electronics, pack: Pack
) -> dict[str, float]:
    """Fault-case peak: all motors and servos stalled at the same time."""
    motor_stall_w = (
        rover.wheels * motor.stall_current_a * motor.rated_voltage_v
    )
    servo_stall_w = (
        electronics.servo_count
        * electronics.servo_stall_a
        * electronics.servo_voltage_v
        / electronics.bec_efficiency
    )
    five_v_w = electronics_power(electronics)["five_v_battery_w"]
    total_w = motor_stall_w + servo_stall_w + five_v_w
    battery_current = total_w / pack.voltage_v
    return {
        "motor_stall_w": motor_stall_w,
        "servo_stall_w": servo_stall_w,
        "electronics_w": five_v_w,
        "total_w": total_w,
        "battery_current_a": battery_current,
        "cell_current_a": battery_current / pack.parallel_strings,
    }


def build_report() -> dict[str, object]:
    rover = Rover()
    motor = Motor()
    electronics = Electronics()
    solar = Solar()

    drive = drive_power(rover, motor)
    elec = electronics_power(electronics)

    idle_w = elec["total_battery_w"]
    cruise_w = idle_w + drive["flat_total_w"]
    slope_w = idle_w + drive["slope_total_w"]

    profiles = mission_profiles(idle_w, cruise_w, slope_w)
    mission_45 = profiles[2]["energy_wh"]
    packs = pack_table(PACKS, profiles[2]["average_w"], mission_45)
    solar_result = solar_table(solar, cruise_w, mission_45)
    peak = peak_power(rover, motor, electronics, PACKS[1])

    return {
        "assumptions": {
            "rover": asdict(rover),
            "motor": asdict(motor),
            "electronics": asdict(electronics),
            "solar": asdict(solar),
        },
        "drive": drive,
        "electronics": elec,
        "modes": {
            "idle_w": idle_w,
            "cruise_w": cruise_w,
            "slope_w": slope_w,
        },
        "missions": profiles,
        "packs": packs,
        "solar": solar_result,
        "peak": peak,
        "steering": steering_table(),
    }


def print_report(report: dict[str, object]) -> None:
    """Print a compact Markdown report (English labels, SI units)."""
    modes = report["modes"]
    drive = report["drive"]
    elec = report["electronics"]
    solar = report["solar"]
    peak = report["peak"]

    print("# Energy budget (preliminary)\n")
    print("## Average loads")
    print("| Load | Power (W) |")
    print("|---|---:|")
    for name, value in elec["five_v_loads"].items():
        print(f"| {name} (at 5 V rail) | {value:.2f} |")
    print(f"| 5 V rail total at battery (converter losses included) | {elec['five_v_battery_w']:.2f} |")
    print(f"| 6 steering servos (average) | {elec['servo_battery_w']:.2f} |")
    print(f"| **Electronics subtotal** | **{modes['idle_w']:.2f}** |")
    print(f"| **Cruise (electronics + drive)** | **{modes['cruise_w']:.2f}** |")
    print(f"| **10 deg slope (electronics + drive)** | **{modes['slope_w']:.2f}** |")
    print()

    print("## Drive model")
    print("| Quantity | Value |")
    print("|---|---:|")
    print(f"| Rolling force | {drive['rolling_force_n']:.2f} N |")
    print(f"| Slope force (10 deg) | {drive['slope_force_n']:.2f} N |")
    print(f"| Flat mechanical power | {drive['flat_mechanical_w']:.2f} W |")
    print(f"| Slope mechanical power | {drive['slope_mechanical_w']:.2f} W |")
    print(f"| Motor no-load power (6 motors) | {drive['no_load_w']:.2f} W |")
    print()

    print("## Mission energy")
    print("| Profile | Average (W) | Energy (Wh) |")
    print("|---|---:|---:|")
    for profile in report["missions"]:
        print(
            f"| {profile['name']} | {profile['average_w']:.2f} | "
            f"{profile['energy_wh']:.2f} |"
        )
    print()

    print("## Battery options (80 % DoD)")
    print("| Pack | Cells | Energy (Wh) | Usable (Wh) | Runtime (h) | 45 min missions | Cell current (A) |")
    print("|---|---:|---:|---:|---:|---:|---:|")
    for pack in report["packs"]:
        print(
            f"| {pack['name']} | {pack['cells']} | {pack['energy_wh']:.1f} | "
            f"{pack['usable_wh']:.1f} | {pack['runtime_h']:.2f} | "
            f"{pack['missions']:.1f} | {pack['cell_current_a']:.2f} |"
        )
    print()

    print("## Solar balance")
    print("| Quantity | Value |")
    print("|---|---:|")
    print(f"| Panel STC power (4 x 7.2 V x 0.6 A) | {solar['p_stc_w']:.2f} W |")
    print(f"| Effective at noon if 600 mA is Imp | {solar['p_effective_imp_w']:.2f} W |")
    print(f"| Effective at noon if 600 mA is Isc | {solar['p_effective_isc_w']:.2f} W |")
    print(f"| Daily energy, Imp case (3 h) | {solar['daily_imp_wh']:.1f} Wh |")
    print(f"| Daily energy, Isc case (3 h) | {solar['daily_isc_wh']:.1f} Wh |")
    print(f"| Deficit vs cruise (Isc case) | {solar['deficit_isc_w']:.2f} W |")
    print(f"| 45 min missions per day (Isc case) | {solar['missions_per_day_isc']:.1f} |")
    print(f"| Required 2S charge voltage | {solar['charge_voltage_v']:.1f} V |")
    print()

    print("## Steering torque per wheel (static, SF = 2)")
    print("| Mass (kg) | Normal force (N) | Torque (kg.cm) | MG90S 2.2 | MG995 10 | 20 kg class |")
    print("|---:|---:|---:|---|---|---|")

    def verdict(torque: float, limit: float) -> str:
        if torque <= 0.8 * limit:
            return "OK"
        if torque <= limit:
            return "MARGINAL"
        return "NO"

    for row in report["steering"]:
        print(
            f"| {row['mass_kg']:.0f} | {row['normal_force_n']:.2f} | "
            f"{row['torque_kgcm']:.2f} | {verdict(row['torque_kgcm'], 2.2)} | "
            f"{verdict(row['torque_kgcm'], 10.0)} | "
            f"{verdict(row['torque_kgcm'], 20.0)} |"
        )
    print()

    print("## Fault-case peak")
    print("| Quantity | Value |")
    print("|---|---:|")
    print(f"| Motors stalled | {peak['motor_stall_w']:.1f} W |")
    print(f"| Servos stalled | {peak['servo_stall_w']:.1f} W |")
    print(f"| Electronics | {peak['electronics_w']:.1f} W |")
    print(f"| Total peak | {peak['total_w']:.1f} W |")
    print(f"| Battery current (2S2P) | {peak['battery_current_a']:.1f} A |")
    print(f"| Current per cell (2S2P) | {peak['cell_current_a']:.1f} A |")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json",
        action="store_true",
        help="print machine-readable JSON instead of Markdown",
    )
    args = parser.parse_args()

    report = build_report()
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print_report(report)


if __name__ == "__main__":
    main()
