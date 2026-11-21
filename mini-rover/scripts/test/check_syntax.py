#!/usr/bin/env python3
"""Check syntax of Python, Bash, YAML, XML/URDF/SDF and JSON files."""

from __future__ import annotations

import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {"build", "install", "log", "__pycache__", ".git", ".venv", "node_modules"}


def files(suffixes: tuple[str, ...]) -> list[Path]:
    result: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in suffixes:
            result.append(path)
    return sorted(result)


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def check_python() -> tuple[int, list[str]]:
    errors: list[str] = []
    paths = files((".py",))
    for path in paths:
        try:
            source = path.read_text(encoding="utf-8")
            compile(source, str(path), "exec")
        except (SyntaxError, UnicodeDecodeError) as exc:
            errors.append(f"{rel(path)}: {exc}")
    return len(paths), errors


def check_bash() -> tuple[int, list[str]]:
    errors: list[str] = []
    paths = files((".sh",))
    for path in paths:
        proc = subprocess.run(
            ["bash", "-n", str(path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            errors.append(f"{rel(path)}: {proc.stderr.strip()}")
    return len(paths), errors


def check_yaml() -> tuple[int, list[str]]:
    errors: list[str] = []
    paths = files((".yaml", ".yml", ".rviz"))
    for path in paths:
        try:
            content = path.read_text(encoding="utf-8")
            if content.strip():
                yaml.safe_load(content)
        except yaml.YAMLError as exc:
            errors.append(f"{rel(path)}: {exc}")
        except UnicodeDecodeError as exc:
            errors.append(f"{rel(path)}: {exc}")
    return len(paths), errors


def check_xml() -> tuple[int, list[str]]:
    errors: list[str] = []
    paths = files((".xml", ".urdf", ".xacro", ".sdf"))
    for path in paths:
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            errors.append(f"{rel(path)}: {exc}")
    return len(paths), errors


def check_json() -> tuple[int, list[str]]:
    errors: list[str] = []
    paths = files((".json",))
    for path in paths:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{rel(path)}: {exc}")
    return len(paths), errors


def main() -> int:
    checks = [
        ("Python", check_python),
        ("Bash", check_bash),
        ("YAML", check_yaml),
        ("XML/URDF/SDF", check_xml),
        ("JSON", check_json),
    ]
    all_errors: list[str] = []
    for label, check in checks:
        count, errors = check()
        print(f"{label}: {count} file(s), {len(errors)} error(s)")
        all_errors.extend(errors)

    for error in all_errors:
        print(f"ERROR: {error}")
    if all_errors:
        print(f"\nFAILED: {len(all_errors)} syntax error(s)")
        return 1
    print("\nOK: all syntax checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
