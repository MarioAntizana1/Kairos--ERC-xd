#!/usr/bin/env bash
# Seal an evidence folder by writing a SHA-256 manifest of its contents.
set -euo pipefail

DIR="${1:-}"
if [ -z "$DIR" ]; then
  echo "Usage: bash scripts/evidence/seal_evidence.sh <evidence-directory>" >&2
  exit 2
fi
if [ ! -d "$DIR" ]; then
  echo "ERROR: not a directory: $DIR" >&2
  exit 1
fi

cd "$DIR"
find . -type f ! -name 'MANIFEST.sha256' -print0 \
  | sort -z \
  | xargs -0 sha256sum > MANIFEST.sha256

if [ ! -s MANIFEST.sha256 ]; then
  echo "ERROR: manifest is empty" >&2
  exit 1
fi

echo "Sealed: $DIR/MANIFEST.sha256"
echo "Manifest hash:"
sha256sum MANIFEST.sha256
