#!/usr/bin/env bash
# Seal an evidence folder with SHA-256. Usage: seal_evidence.sh "<dir>"
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Uso: $0 <carpeta-de-evidencia>" >&2
  exit 2
fi

DIR="$1"
if [[ ! -d "$DIR" ]]; then
  echo "ERROR: no existe la carpeta $DIR" >&2
  exit 1
fi

(
  cd "$DIR"
  find . -type f ! -name MANIFEST.sha256 -print0 \
    | sort -z \
    | xargs -0 sha256sum > MANIFEST.sha256
)

echo "Manifest: $DIR/MANIFEST.sha256"
sha256sum "$DIR/MANIFEST.sha256"
