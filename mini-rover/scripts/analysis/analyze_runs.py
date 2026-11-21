#!/usr/bin/env python3
"""Summarise mission test results from a CSV file.

The CSV schema is documented in docs/06-pruebas/resultados/README.md. The
script uses only the Python standard library.

Usage:
    python3 scripts/analysis/analyze_runs.py runs.csv
    python3 scripts/analysis/analyze_runs.py runs.csv --output analisis.md
"""

from __future__ import annotations

import argparse
import csv
import math
import statistics
import sys
from pathlib import Path
from typing import Iterable


def parse_float(value: str | None) -> float | None:
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    try:
        number = float(value)
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def parse_success(value: str | None) -> int | None:
    if value is None:
        return None
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y", "pass", "passed"}:
        return 1
    if normalized in {"0", "false", "no", "n", "fail", "failed"}:
        return 0
    return None


def wilson_interval(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    if total <= 0:
        return (0.0, 0.0)
    p = successes / total
    denominator = 1.0 + z * z / total
    centre = (p + z * z / (2.0 * total)) / denominator
    margin = z * math.sqrt((p * (1.0 - p) / total) + (z * z / (4.0 * total * total))) / denominator
    return (max(0.0, centre - margin), min(1.0, centre + margin))


def percentile(values: list[float], fraction: float) -> float:
    if not values:
        raise ValueError("percentile of empty list")
    ordered = sorted(values)
    index = max(0, min(len(ordered) - 1, math.ceil(fraction * len(ordered)) - 1))
    return ordered[index]


def describe(values: Iterable[float | None]) -> str:
    numbers = [float(value) for value in values if value is not None]
    if not numbers:
        return "—"
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    stdev = statistics.stdev(numbers) if len(numbers) > 1 else 0.0
    p95 = percentile(numbers, 0.95)
    return (
        f"media {mean:.2f}, mediana {median:.2f}, sd {stdev:.2f}, "
        f"p95 {p95:.2f}, min {min(numbers):.2f}, max {max(numbers):.2f} "
        f"(n={len(numbers)})"
    )


def subset(rows: list[dict[str, str]], key: str, value: str) -> list[dict[str, str]]:
    return [row for row in rows if row.get(key, "").strip() == value]


def block(rows: list[dict[str, str]], title: str) -> list[str]:
    lines = [f"### {title}", ""]
    successes = [parse_success(row.get("success")) for row in rows]
    valid_success = [item for item in successes if item is not None]
    completed = sum(valid_success)
    total = len(valid_success)
    if total:
        low, high = wilson_interval(completed, total)
        lines.append(
            f"- **Éxito:** {completed}/{total} = {100.0 * completed / total:.1f}% "
            f"(IC 95% Wilson: {100.0 * low:.1f}%–{100.0 * high:.1f}%)"
        )
    else:
        lines.append("- **Éxito:** sin datos")

    collisions = sum(
        int(value) for row in rows
        if (value := parse_float(row.get("collisions"))) is not None
    )
    interventions = sum(
        int(value) for row in rows
        if (value := parse_float(row.get("interventions"))) is not None
    )
    lines.append(f"- **Colisiones:** {collisions}")
    lines.append(f"- **Intervenciones humanas:** {interventions}")
    lines.append(f"- **Error final (m):** {describe(parse_float(row.get('final_error_m')) for row in rows)}")
    lines.append(
        f"- **Error de orientación (rad):** "
        f"{describe(parse_float(row.get('final_yaw_error_rad')) for row in rows)}"
    )
    lines.append(f"- **Duración (s):** {describe(parse_float(row.get('duration_s')) for row in rows)}")
    lines.append(f"- **CPU media (%):** {describe(parse_float(row.get('cpu_mean_pct')) for row in rows)}")
    lines.append(f"- **Temperatura pico (°C):** {describe(parse_float(row.get('temp_peak_c')) for row in rows)}")
    lines.append("")

    lines.append("| run_id | entorno | éxito | error final (m) | duración (s) | notas |")
    lines.append("|---|---|---|---|---|---|")
    for row in rows:
        lines.append(
            "| {run} | {env} | {success} | {error} | {duration} | {notes} |".format(
                run=row.get("run_id", "—"),
                env=row.get("environment", "—"),
                success=row.get("success", "—"),
                error=row.get("final_error_m", "—"),
                duration=row.get("duration_s", "—"),
                notes=(row.get("notes", "") or "").replace("|", "/"),
            )
        )
    lines.append("")
    return lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path, help="CSV with one row per run")
    parser.add_argument("--output", type=Path, help="write the Markdown report to this file")
    args = parser.parse_args(argv)

    if not args.csv_file.exists():
        print(f"ERROR: file not found: {args.csv_file}", file=sys.stderr)
        return 1

    with args.csv_file.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        print("ERROR: CSV has no data rows", file=sys.stderr)
        return 1

    lines = [
        "# Análisis de ensayos",
        "",
        f"- Archivo: `{args.csv_file}`",
        f"- Ensayos: {len(rows)}",
        "",
        "## Global",
        "",
    ]
    lines.extend(block(rows, "Todos los ensayos").copy())

    environments = sorted({row.get("environment", "").strip() or "unknown" for row in rows})
    if len(environments) > 1:
        lines.extend(["## Por entorno", ""])
        for environment in environments:
            lines.extend(block(subset(rows, "environment", environment), environment))
            lines.append("")

    report = "\n".join(lines).rstrip() + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
