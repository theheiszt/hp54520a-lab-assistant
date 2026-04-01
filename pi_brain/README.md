# Pi Brain

This directory contains the higher-level lab assistant services.

## Responsibilities

- subscribe to instrument telemetry over MQTT
- retain recent measurements and events
- expose a small HTTP API for dashboards and agent tooling
- generate first-pass diagnostic suggestions before any LLM layer is added

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api_main:app --host 0.0.0.0 --port 8000
```

## First API endpoints

- `/health`
- `/scope/latest`
- `/scope/suggestions`
- `/scope/history`
