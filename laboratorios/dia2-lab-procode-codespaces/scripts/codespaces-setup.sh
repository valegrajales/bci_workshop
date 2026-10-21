#!/usr/bin/env bash
# Se ejecuta una vez al crear el Codespace (postCreateCommand). Prepara Python 3.12 y el archivo .env.
set -euo pipefail

cd "$(dirname "$0")/.."

echo "==> Python: $(python --version)"
python -m pip install --upgrade pip --quiet
python -m pip install -r requirements-dev.txt --quiet

if [ ! -f .env ]; then
  cp .env.example .env
  echo "==> .env creado desde .env.example: completa los valores que te entregan los instructores."
fi

echo "==> Azure CLI: $(az version --query '"azure-cli"' -o tsv 2>/dev/null || echo 'no disponible')"
python -m pip list --format=freeze 2>/dev/null | grep -E '^(agent-framework-foundry|azure-search-documents|azure-identity|azure-monitor-opentelemetry)==' || true
echo "==> Listo. Siguiente paso: az login --use-device-code (ver README, seccion 5)."
