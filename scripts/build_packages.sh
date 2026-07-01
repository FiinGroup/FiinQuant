#!/usr/bin/env bash
# Đóng gói mỗi skill thành 1 file .zip để phân phối cho môi trường sử dụng skill.
#
# Layout zip: mỗi zip chứa đúng 1 thư mục top-level <skill-name>/ với SKILL.md ở gốc
# thư mục đó.
#
# Cách dùng:  bash scripts/build_packages.sh
# Kết quả:    dist/<skill-name>.zip cho từng skill trong skills/

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

DIST="dist"
rm -rf "$DIST"
mkdir -p "$DIST"

for dir in plugins/*/skills/*/; do
  name="$(basename "$dir")"
  parent="$(dirname "$dir")"          # plugins/<plugin>/skills
  # zip từ trong .../skills để giữ thư mục <name>/ làm top-level trong archive
  ( cd "$parent" && zip -q -r -X "$ROOT/$DIST/$name.zip" "$name" \
      -x '*/.DS_Store' '*/__pycache__/*' )
  echo "  ✓ $DIST/$name.zip"
done

echo "Done. $(ls -1 "$DIST" | wc -l | tr -d ' ') package(s) trong $DIST/"
