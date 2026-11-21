#!/usr/bin/env bash
# Create a new evidence folder with metadata and a report template.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SLUG_RAW="${1:-manual}"
SLUG="$(printf '%s' "$SLUG_RAW" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"
[ -n "$SLUG" ] || SLUG="manual"

DATE="$(date +%Y-%m-%d)"
STAMP="$(date +%Y-%m-%dT%H%M%S)"
BASE="$ROOT/docs/08-evidencia/artefactos"
mkdir -p "$BASE"

COUNT="$(find "$BASE" -maxdepth 1 -type d -name "${DATE}T*" | wc -l | tr -d ' ')"
ID="$(printf 'EV-%s-%02d' "$DATE" "$((COUNT + 1))")"
DIR="$BASE/$STAMP-$SLUG"

if [ -e "$DIR" ]; then
  echo "ERROR: evidence directory already exists: $DIR" >&2
  exit 1
fi

mkdir -p "$DIR/logs" "$DIR/media" "$DIR/bags"
touch "$DIR/logs/.gitkeep" "$DIR/media/.gitkeep" "$DIR/bags/.gitkeep"

export EVIDENCE_DIR="$DIR"
export EVIDENCE_ID="$ID"
export EVIDENCE_SLUG="$SLUG"
export EVIDENCE_DATE="$DATE"
export EVIDENCE_ROOT="$ROOT"

python3 - <<'PY'
"""Write metadata.json and README.md for a new evidence folder."""
from __future__ import annotations

import json
import os
import platform
import socket
import subprocess
from datetime import datetime, timezone
from pathlib import Path

root = Path(os.environ["EVIDENCE_ROOT"])
directory = Path(os.environ["EVIDENCE_DIR"])


def git(*args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args],
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )
    except Exception:
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def gz_version() -> str | None:
    try:
        result = subprocess.run(
            ["gz", "sim", "--versions"],
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )
    except Exception:
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip().splitlines()[0] if result.stdout.strip() else None


dirty = git("status", "--porcelain")
metadata = {
    "id": os.environ["EVIDENCE_ID"],
    "date": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
    "slug": os.environ["EVIDENCE_SLUG"],
    "operator": os.environ.get("USER", "unknown"),
    "host": socket.gethostname(),
    "os": platform.platform(),
    "kernel": platform.release(),
    "architecture": platform.machine(),
    "python": platform.python_version(),
    "ros_distro": os.environ.get("ROS_DISTRO"),
    "gazebo": gz_version(),
    "commit": git("rev-parse", "--short", "HEAD"),
    "dirty": bool(dirty),
    "command": None,
    "requirements": [],
    "tests": [],
    "result": "pending",
    "notes": "Complete this file after running the test or demo.",
}

(directory / "metadata.json").write_text(
    json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)

readme = f"""# Evidencia {os.environ['EVIDENCE_ID']} — {os.environ['EVIDENCE_SLUG']}

> Fecha: {os.environ['EVIDENCE_DATE']} · Estado: Pendiente · Responsable: {os.environ.get('USER', 'unknown')}

## 1. Objetivo

Describe qué se quería demostrar y por qué.

## 2. Requisitos y casos

- Requisitos:
- Casos de prueba:

## 3. Entorno

Ver `metadata.json`. Añade aquí cualquier detalle relevante (hardware, versión de Gazebo, batería, etc.).

## 4. Comando ejecutado

```bash
# Pega aquí el comando exacto
```

## 5. Resultado

| Métrica | Valor | Umbral | Veredicto |
|---|---|---|---|
| | | | |

## 6. Artefactos

| Archivo | Descripción |
|---|---|
| `logs/` | Salidas de consola |
| `media/` | Capturas, fotos o vídeo |
| `bags/` | Rosbag2 (o enlace externo) |

## 7. Conclusión

- [ ] Aprobado
- [ ] Aprobado con desviación
- [ ] Fallido
- [ ] Inconcluso

## 8. Reproducibilidad

Pasos para repetir la ejecución y comprobar el resultado.

## 9. Sellar

```bash
bash scripts/evidence/seal_evidence.sh "{directory}"
```
"""
(directory / "README.md").write_text(readme, encoding="utf-8")
print(f"Created {directory}")
print(f"ID: {os.environ['EVIDENCE_ID']}")
PY

echo
echo "Evidence folder: $DIR"
echo "Next:"
echo "  1. Run the test/demo and save logs in $DIR/logs"
echo "  2. Fill README.md and metadata.json"
echo "  3. Seal: bash scripts/evidence/seal_evidence.sh \"$DIR\""
echo "  4. Register it in docs/08-evidencia/registro-evidencias.md"
