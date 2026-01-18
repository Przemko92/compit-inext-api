#!/usr/bin/env bash
set -euo pipefail

# Builds and uploads the package to PyPI using Twine.
# Token is read from PYPI_API_TOKEN (recommended) or interactively prompted.
#
# Usage:
#   bash scripts/publish.sh
#   PYPI_API_TOKEN=pypi-... bash scripts/publish.sh
#
# If a `.env` file exists in the repo root, it will be loaded automatically.
#
# Optional:
#   TWINE_REPOSITORY_URL=https://test.pypi.org/legacy/ bash scripts/publish.sh

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  sed -n '1,80p' "$0" | sed 's/^# \{0,1\}//'
  exit 0
fi

# Load token from .env if present (gitignored by default).
if [[ -f "$ROOT_DIR/.env" ]]; then
  set -o allexport
  # shellcheck disable=SC1091
  source "$ROOT_DIR/.env"
  set +o allexport
fi

if ! command -v python >/dev/null 2>&1; then
  echo "python not found in PATH" >&2
  exit 1
fi

if [[ -z "${PYPI_API_TOKEN:-}" ]]; then
  echo "PYPI_API_TOKEN is not set." >&2
  read -r -s -p "Enter PyPI API token (input hidden): " PYPI_API_TOKEN
  echo
  if [[ -z "$PYPI_API_TOKEN" ]]; then
    echo "Token is empty; aborting." >&2
    exit 1
  fi
fi

# Ensure build tooling is available (does not pin versions).
python -m pip install --upgrade build twine >/dev/null

rm -rf dist

python -m build

twine check dist/*

export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="$PYPI_API_TOKEN"

# Let user override repository via TWINE_REPOSITORY_URL / TWINE_REPOSITORY.
twine upload dist/*
