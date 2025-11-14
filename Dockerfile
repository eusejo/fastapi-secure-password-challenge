FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv pip sync --system --no-cache

COPY src/ ./src/

EXPOSE 8000

CMD ["uvicorn", "app.api:app", "--app-dir", "src", "--host", "0.0.0.0", "--port", "8000"]
