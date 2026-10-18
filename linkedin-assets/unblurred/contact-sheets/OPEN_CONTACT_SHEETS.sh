#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
VIEWER="${IMAGE_VIEWER:-ristretto}"

if ! command -v "$VIEWER" >/dev/null 2>&1; then
  VIEWER=xdg-open
fi

if ! command -v "$VIEWER" >/dev/null 2>&1; then
  printf 'No image viewer found. Install ristretto or open the PNG files from your file manager.\n' >&2
  exit 1
fi

if [[ "$VIEWER" == ristretto ]]; then
  exec "$VIEWER" "$DIR"/*.png
fi

for image in "$DIR"/*.png; do
  "$VIEWER" "$image" >/dev/null 2>&1 &
done
