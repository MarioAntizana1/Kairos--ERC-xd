#!/usr/bin/env bash
# Create an evidence folder with metadata. Usage: new_evidence.sh "<slug>"
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SLUG="${1:-validacion}"
SLUG="$(printf '%s' "$SLUG" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')"
STAMP="$(date +%Y-%m-%dT%H%M%S)"
DIR="$ROOT/docs/08-evidencia/artefactos/${STAMP}-${SLUG}"

mkdir -p "$DIR"/logs "$DIR"/media "$DIR"/bags

if git -C "$ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  COMMIT="$(git -C "$ROOT" rev-parse --short HEAD)"
  DIRTY="$(git -C "$ROOT" status --porcelain | wc -l | tr -d ' ')"
else
  COMMIT="no-git"
  DIRTY="unknown"
fi

cat > "$DIR/README.md" <<EOF
# Evidencia ${STAMP}-${SLUG}

> Estado: Pendiente · Fecha: ${STAMP} · Responsable: QA

## Objetivo

<Describir la pregunta o el criterio que se quiere verificar.>

## Entorno

- Host: $(hostname)
- SO: $(uname -sr)
- Python: $(python3 --version 2>&1 || echo "no disponible")
- Commit: ${COMMIT}

## Comando

\`\`\`bash
<comando exacto>
\`\`\`

## Resultado

<Pendiente de ejecución.>

## Conclusión

<Pendiente.>

## Limitaciones

<Qué no cubre esta evidencia.>
EOF

cat > "$DIR/metadata.json" <<EOF
{
  "id": "EV-${STAMP:0:10}-01",
  "date": "$(date -Iseconds)",
  "operator": "QA",
  "host": "$(hostname)",
  "os": "$(uname -sr)",
  "python": "$(python3 --version 2>&1 | sed 's/^Python //')",
  "commit": "${COMMIT}",
  "dirty": "${DIRTY}",
  "command": "<comando exacto>",
  "requirements": [],
  "tests": [],
  "result": "pending"
}
EOF

echo "$DIR"
