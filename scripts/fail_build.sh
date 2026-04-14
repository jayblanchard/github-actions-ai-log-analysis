#!/usr/bin/env bash
set -euo pipefail

echo "Resolving dependencies..."
sleep 1

echo "WARNING: deprecated package detected"
sleep 1

echo "ERROR: Failed to resolve dependency foo-bar:1.2.3"

exit 1