#!/usr/bin/env bash
#
# test.sh — run the practice tests. Sets up the test tool for you the first time.
#
# Usage:
#   ./test.sh                                          # run every test in the repo
#   ./test.sh assessment                               # just the assessment tests
#   ./test.sh curriculum/mit-6.0001/ps1-credit-card-debt   # just one assignment
#
# Tests are RED until you fill in the code — that's the point. Turning them green
# IS the exercise. 🙂
#
set -euo pipefail

# Work from the repo root so the local .venv is always found.
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VENV=".venv"

# First run: build a tiny private environment and install pytest into it.
# This keeps your Mac's Python clean and means the tests "just work".
if [[ ! -x "$VENV/bin/python" ]]; then
  echo "Setting up the test tool for the first time (about 20 seconds)…"
  python3 -m venv "$VENV"
  "$VENV/bin/python" -m pip install --quiet --upgrade pip
  "$VENV/bin/python" -m pip install --quiet pytest
  echo "Done — tests are ready."
fi

# Safety net: if the venv exists but pytest somehow isn't there, add it.
if ! "$VENV/bin/python" -m pytest --version >/dev/null 2>&1; then
  "$VENV/bin/python" -m pip install --quiet pytest
fi

exec "$VENV/bin/python" -m pytest "$@"
