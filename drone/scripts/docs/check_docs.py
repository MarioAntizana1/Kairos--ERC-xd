#!/usr/bin/env python3
"""Validate documentation links, requirement IDs, ADRs and evidence paths."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"

REQUIRED = [
    "README.md",
    "glosario.md",
    "00-gobierno/metodologia.md",
    "00-gobierno/plan-proyecto.md",
    "00-gobierno/roles-y-raci.md",
    "00-gobierno/gestion-riesgos.md",
    "00-gobierno/registro-decisiones.md",
    "00-gobierno/plantillas/adr.md",
    "00-gobierno/plantillas/requisito.md",
    "00-gobierno/plantillas/caso-prueba.md",
    "00-gobierno/plantillas/informe-evidencia.md",
    "01-investigacion/contexto-drone.md",
    "01-investigacion/estado-del-arte.md",
    "01-investigacion/hipotesis-y-experimentos.md",
    "01-investigacion/normativa-y-seguridad.md",
    "01-investigacion/fuentes.md",
    "02-requisitos/vision-alcance.md",
    "02-requisitos/requisitos-funcionales.md",
    "02-requisitos/requisitos-no-funcionales.md",
    "02-requisitos/historias-usuario.md",
    "02-requisitos/trazabilidad.md",
    "03-arquitectura/arquitectura-vision.md",
    "03-arquitectura/interfaces.md",
    "03-arquitectura/seguridad.md",
    "03-arquitectura/adr/0001-pi5-computo.md",
    "03-arquitectura/adr/0002-stereo-cm3.md",
    "03-arquitectura/adr/0003-tof-vl53l5cx.md",
    "03-arquitectura/adr/0004-pipeline-stereo.md",
    "03-arquitectura/adr/0005-evidencia-reproducible.md",
    "04-diseno/diseno-vision.md",
    "04-diseno/bom.md",
    "04-diseno/bom-peru.md",
    "05-implementacion/entorno-desarrollo.md",
    "05-implementacion/guia-instalacion.md",
    "05-implementacion/bitacora.md",
    "06-pruebas/plan-pruebas.md",
    "06-pruebas/casos-prueba.md",
    "06-pruebas/protocolo-experimentos.md",
    "06-pruebas/matriz-trazabilidad-pruebas.md",
    "06-pruebas/resultados/README.md",
    "06-pruebas/resultados/plantilla-datos.csv",
    "07-operacion/runbook-vuelo.md",
    "07-operacion/mantenimiento.md",
    "08-evidencia/README.md",
    "08-evidencia/registro-evidencias.md",
    "09-presentacion/guion-demo.md",
]

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
REQ_ID_RE = re.compile(r"\b(RF-\d{2}|RNF-\d{2})\b")
TC_ID_RE = re.compile(r"\b(TC-\d{2})\b")
TABLE_REQ_RE = re.compile(r"^\|\s*(RF-\d{2}|RNF-\d{2})\s*\|", re.MULTILINE)
HEADING_REQ_RE = re.compile(r"^###\s+(RF-\d{2}|RNF-\d{2})\b", re.MULTILINE)
TABLE_TC_RE = re.compile(r"^\|\s*(TC-\d{2})\s*\|", re.MULTILINE)
HEADING_TC_RE = re.compile(r"^###\s+(TC-\d{2})\b", re.MULTILINE)
TABLE_SOURCE_RE = re.compile(r"^\|\s*(F-\d{2,3})\s*\|", re.MULTILINE)
SOURCE_ID_RE = re.compile(r"\b(F-\d{2,3})\b")
HOME_PATH_RE = re.compile(r"(/home/[A-Za-z0-9._-]+|/Users/[A-Za-z0-9._-]+)")


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def strip_non_links(text: str) -> str:
    text = FENCED_CODE_RE.sub("", text)
    text = INLINE_CODE_RE.sub("", text)
    return text


def markdown_files() -> list[Path]:
    files = list(ROOT.glob("*.md")) + list(DOCS.rglob("*.md"))
    return sorted(set(files))


def check_links(files: list[Path]) -> tuple[int, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    checked = 0
    for path in files:
        text = strip_non_links(path.read_text(encoding="utf-8"))
        for target in LINK_RE.findall(text):
            target = target.strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:", "//")):
                continue
            target = target.split("#", 1)[0].strip()
            if not target:
                continue
            checked += 1
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{relative(path)}: broken link -> {target}")
        if HOME_PATH_RE.search(text):
            warnings.append(f"{relative(path)}: contains an absolute home path")
    return checked, errors, warnings


def collect_requirements() -> tuple[set[str], set[str], set[str]]:
    defined: set[str] = set()
    referenced: set[str] = set()
    for name in (
        "02-requisitos/requisitos-funcionales.md",
        "02-requisitos/requisitos-no-funcionales.md",
    ):
        text = (DOCS / name).read_text(encoding="utf-8")
        defined.update(TABLE_REQ_RE.findall(text))
        defined.update(HEADING_REQ_RE.findall(text))
    for path in markdown_files():
        referenced.update(REQ_ID_RE.findall(path.read_text(encoding="utf-8")))
    traceability = (DOCS / "02-requisitos/trazabilidad.md").read_text(encoding="utf-8")
    traced = set(TABLE_REQ_RE.findall(traceability))
    return defined, referenced, traced


def collect_sources() -> tuple[set[str], set[str]]:
    source_text = (DOCS / "01-investigacion/fuentes.md").read_text(encoding="utf-8")
    defined = set(TABLE_SOURCE_RE.findall(source_text))
    referenced: set[str] = set()
    for path in markdown_files():
        referenced.update(SOURCE_ID_RE.findall(path.read_text(encoding="utf-8")))
    return defined, referenced


def collect_test_cases() -> tuple[set[str], set[str]]:
    text = (DOCS / "06-pruebas/casos-prueba.md").read_text(encoding="utf-8")
    defined = set(TABLE_TC_RE.findall(text)) | set(HEADING_TC_RE.findall(text))
    referenced: set[str] = set()
    for path in markdown_files():
        referenced.update(TC_ID_RE.findall(path.read_text(encoding="utf-8")))
    return defined, referenced


def check_adrs() -> list[str]:
    errors: list[str] = []
    adr_dir = DOCS / "03-arquitectura/adr"
    adr_files = sorted(adr_dir.glob("*.md"))
    index = (DOCS / "00-gobierno/registro-decisiones.md").read_text(encoding="utf-8")
    numbers: list[str] = []
    for path in adr_files:
        match = re.match(r"^(\d{4})-", path.name)
        if not match:
            errors.append(f"{relative(path)}: ADR filename must start with 4 digits")
            continue
        numbers.append(match.group(1))
        if path.name not in index:
            errors.append(f"{relative(path)}: not listed in registro-decisiones.md")
        text = path.read_text(encoding="utf-8")
        if "Estado:" not in text:
            errors.append(f"{relative(path)}: missing 'Estado:' header")
    if len(numbers) != len(set(numbers)):
        errors.append("duplicate ADR numbers")
    return errors


def check_evidence_paths() -> list[str]:
    errors: list[str] = []
    registry = DOCS / "08-evidencia/registro-evidencias.md"
    for line in registry.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| EV-"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 9:
            errors.append(f"evidence registry: malformed row -> {line[:80]}")
            continue
        path_cell = cells[6].strip("`")
        if path_cell in {"", "—", "-"} or path_cell.startswith("http"):
            continue
        candidate = (DOCS / "08-evidencia" / path_cell).resolve()
        if not candidate.exists():
            errors.append(f"evidence registry: path not found -> {path_cell}")
    return errors


def check_status_headers(files: list[Path]) -> list[str]:
    warnings: list[str] = []
    skip_parts = {"plantillas", "08-evidencia"}
    for path in files:
        if path.name in {"README.md", "AGENTS.md", "CHANGELOG.md"}:
            continue
        if any(part in skip_parts for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        if "Estado:" not in text:
            warnings.append(f"{relative(path)}: missing 'Estado:' header")
    return warnings


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for name in REQUIRED:
        if not (DOCS / name).exists():
            errors.append(f"missing required document: docs/{name}")

    artefacts = DOCS / "08-evidencia/artefactos"
    if not artefacts.exists():
        errors.append("missing docs/08-evidencia/artefactos/")

    files = markdown_files()
    links_checked, link_errors, link_warnings = check_links(files)
    errors.extend(link_errors)
    warnings.extend(link_warnings)

    defined, referenced, traced = collect_requirements()
    missing_trace = sorted(defined - traced)
    if missing_trace:
        errors.append(f"requirements missing from traceability: {', '.join(missing_trace)}")
    undefined = sorted(referenced - defined)
    if undefined:
        errors.append(f"undefined requirement IDs referenced: {', '.join(undefined)}")
    extra_trace = sorted(traced - defined)
    if extra_trace:
        errors.append(f"traceability references undefined IDs: {', '.join(extra_trace)}")

    source_defined, source_referenced = collect_sources()
    undefined_sources = sorted(source_referenced - source_defined)
    if undefined_sources:
        errors.append(f"source IDs referenced but not registered: {', '.join(undefined_sources)}")

    tc_defined, tc_referenced = collect_test_cases()
    undefined_tc = sorted(tc_referenced - tc_defined)
    if undefined_tc:
        errors.append(f"undefined test case IDs referenced: {', '.join(undefined_tc)}")

    errors.extend(check_adrs())
    errors.extend(check_evidence_paths())
    warnings.extend(check_status_headers(files))

    print(f"Docs scanned: {len(files)}")
    print(f"Local links checked: {links_checked}")
    print(
        "Functional/NFR IDs: "
        f"{len([i for i in defined if i.startswith('RF-')])}/"
        f"{len([i for i in defined if i.startswith('RNF-')])}"
    )
    print(f"Test cases: {len(tc_defined)}")
    print(f"Sources: {len(source_defined)}")
    print(f"ADRs: {len(list((DOCS / '03-arquitectura/adr').glob('*.md')))}")

    for message in warnings:
        print(f"WARNING: {message}")
    for message in errors:
        print(f"ERROR: {message}")

    if errors:
        print(f"\nFAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"\nOK: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
