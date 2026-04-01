from __future__ import annotations
from contextlib import asynccontextmanager
from fastapi import FastAPI
from mqtt_ingest import ScopeIngestClient
from state_store import StateStore
from suggestion_engine import suggest_next_steps

MQTT_HOST = "127.0.0.1"
MQTT_PORT = 1883
TOPIC_PREFIX = "lab/scope/hp54520a"

store = StateStore()
ingest = ScopeIngestClient(MQTT_HOST, MQTT_PORT, TOPIC_PREFIX, store)


@asynccontextmanager
async def lifespan(app: FastAPI):
    ingest.start()
    yield
    ingest.stop()


app = FastAPI(title="Lab Brain API", lifespan=lifespan)


@app.get("/health")
def health() -> dict:
    return {"ok": True}


@app.get("/scope/latest")
def scope_latest() -> dict:
    return {"message": store.latest()}


@app.get("/scope/suggestions")
def scope_suggestions() -> dict:
    latest = store.latest()
    if not latest:
        return {
            "message": None,
            "suggestions": ["No scope data yet. Check the GPIB node and MQTT broker."],
        }
    return {"message": latest, "suggestions": suggest_next_steps(latest)}


@app.get("/scope/history")
def scope_history() -> dict:
    return {"messages": store.all()}
