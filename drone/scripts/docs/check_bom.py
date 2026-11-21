#!/usr/bin/env python3
"""Validate the Peru BOM CSV: arithmetic, base total and contingency."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "docs/04-diseno/bom-peru.csv"

EXPECTED_BASE = 2229.60
CONTINGENCY_RATE = 0.05
EXPECTED_TOTAL = 2341.08
TOLERANCE = 0.02


def money(value: str) -> float:
    return float(value.strip().replace(" ", "").replace(",", ""))


def main() -> int:
    if not CSV_PATH.exists():
        print(f"ERROR: no existe {CSV_PATH}")
        return 1

    errors: list[str] = []
    base = 0.0
    with CSV_PATH.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {
            "id",
            "grupo",
            "componente",
            "modelo",
            "cantidad",
            "proveedor",
            "precio_unit_pen",
            "subtotal_pen",
            "estado",
            "url",
            "notas",
            "incluir",
        }
        missing = required - set(reader.fieldnames or [])
        if missing:
            print(f"ERROR: columnas faltantes: {', '.join(sorted(missing))}")
            return 1

        for row in reader:
            quantity = int(row["cantidad"])
            unit = money(row["precio_unit_pen"])
            subtotal = money(row["subtotal_pen"])
            if abs(quantity * unit - subtotal) > TOLERANCE:
                errors.append(
                    f"{row['id']}: cantidad × unitario = {quantity * unit:.2f}, "
                    f"subtotal = {subtotal:.2f}"
                )
            if row["incluir"].strip().lower() == "si":
                base += subtotal

    contingency = round(base * CONTINGENCY_RATE, 2)
    total = round(base + contingency, 2)

    print(f"Base (incluir=si): S/ {base:,.2f}")
    print(f"Contingencia 5%:   S/ {contingency:,.2f}")
    print(f"Total:             S/ {total:,.2f}")

    if abs(base - EXPECTED_BASE) > TOLERANCE:
        errors.append(f"base {base:.2f} != esperado {EXPECTED_BASE:.2f}")
    if abs(total - EXPECTED_TOTAL) > TOLERANCE:
        errors.append(f"total {total:.2f} != esperado {EXPECTED_TOTAL:.2f}")

    for message in errors:
        print(f"ERROR: {message}")
    if errors:
        print(f"\nFAILED: {len(errors)} error(s)")
        return 1
    print("\nOK: BOM consistente")
    return 0


if __name__ == "__main__":
    sys.exit(main())
