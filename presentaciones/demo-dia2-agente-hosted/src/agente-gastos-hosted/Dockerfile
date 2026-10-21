# La plataforma de hosted agents exige imágenes linux/amd64.
# Local: docker build --platform linux/amd64 -t agente-gastos:v1 .
FROM ghcr.io/astral-sh/uv:0.11.7 AS uv
FROM python:3.13-slim

COPY --from=uv /uv /uvx /bin/

WORKDIR /app/user_agent
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY main.py limites.py ./

EXPOSE 8088

CMD ["/app/user_agent/.venv/bin/python", "main.py"]
