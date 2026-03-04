#!/usr/bin/env bash
# Test a constraints file against multiple Python versions using uv venvs.
# Usage: ./test_constraints.sh [constraints_file]
# Default constraints file: constraints-testing.txt

set -euo pipefail

CONSTRAINTS="${1:-constraints-testing.txt}"
PYTHON_VERSIONS=(3.10 3.11 3.12 3.13 3.14 3.15)
VENV_BASE=".venvs"
PASS=()
FAIL=()
SKIP=()

if [ ! -f "$CONSTRAINTS" ]; then
  echo "ERROR: constraints file not found: $CONSTRAINTS"
  exit 1
fi

echo "Testing: $CONSTRAINTS"
echo "========================================"

for py in "${PYTHON_VERSIONS[@]}"; do
  venv="$VENV_BASE/py${py}"
  echo ""
  echo "--- Python $py ---"

  # Create venv if it doesn't exist
  if [ ! -d "$venv" ]; then
    if ! uv venv --python "$py" "$venv" 2>/dev/null; then
      echo "SKIP: Python $py not available"
      SKIP+=("$py")
      continue
    fi
  fi

  # Resolve + dry-run install (no network download of packages)
  if uv pip install --python "$venv" --dry-run -r "$CONSTRAINTS" 2>/tmp/uv_err_${py}; then
    echo "PASS"
    PASS+=("$py")
  else
    echo "FAIL:"
    cat /tmp/uv_err_${py}
    FAIL+=("$py")
  fi
done

echo ""
echo "========================================"
echo "Results for: $CONSTRAINTS"
[ ${#PASS[@]}  -gt 0 ] && echo "  PASS : ${PASS[*]}"
[ ${#FAIL[@]}  -gt 0 ] && echo "  FAIL : ${FAIL[*]}"
[ ${#SKIP[@]}  -gt 0 ] && echo "  SKIP : ${SKIP[*]} (Python version not installed)"
echo "========================================"

[ ${#FAIL[@]} -eq 0 ]
