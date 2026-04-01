from __future__ import annotations
import json
from typing import Any, Dict
import paho.mqtt.client as mqtt
from state_store import StateStore


class ScopeIngestClient:
    def __init__(self, host: str, port: int, topic_prefix: str, store: StateStore) -> None:
        self.topic_prefix = topic_prefix.rstrip("/")
        self.store = store
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(host, port, keepalive=30)

    def _on_connect(self, client, userdata, flags, reason_code, properties) -> None:
        client.subscribe(f"{self.topic_prefix}/#")

    def _on_message(self, client, userdata, msg) -> None:
        try:
            payload: Dict[str, Any] = json.loads(msg.payload.decode("utf-8"))
            payload["_topic"] = msg.topic
            self.store.add(payload)
        except Exception as exc:
            self.store.add({
                "kind": "error",
                "data": {"stage": "mqtt_ingest", "error": str(exc)},
                "_topic": msg.topic,
            })

    def start(self) -> None:
        self.client.loop_start()

    def stop(self) -> None:
        self.client.loop_stop()
        self.client.disconnect()
