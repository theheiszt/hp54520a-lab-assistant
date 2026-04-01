from __future__ import annotations
import json
import signal
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from gpib_link import GpibScopeLink
from mqtt_client import MqttPublisher
from scope_adapter import HP54520AAdapter

RUNNING = True


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_config(path: str) -> Dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def stop_handler(signum, frame) -> None:
    global RUNNING
    RUNNING = False


def main() -> int:
    cfg = load_config("config.json")
    signal.signal(signal.SIGINT, stop_handler)
    signal.signal(signal.SIGTERM, stop_handler)

    adapter = HP54520AAdapter()
    link = GpibScopeLink(**cfg["gpib"])
    mqtt = MqttPublisher(**cfg["mqtt"])

    prefix = cfg["mqtt"]["topic_prefix"]
    node_id = cfg["node_id"]
    instrument = cfg["instrument"]
    poll_interval = float(cfg.get("poll_interval_sec", 2.0))

    try:
        try:
            raw = link.query(adapter.commands.identity_query)
            mqtt.publish(
                f"{prefix}/identity",
                {
                    "ts": utc_now(),
                    "node": node_id,
                    "instrument": instrument,
                    "kind": "identity",
                    "data": adapter.parse_identity(raw),
                },
            )
        except Exception as exc:
            mqtt.publish(
                f"{prefix}/events",
                {
                    "ts": utc_now(),
                    "node": node_id,
                    "instrument": instrument,
                    "kind": "error",
                    "data": {"stage": "identity", "error": str(exc)},
                },
            )

        while RUNNING:
            try:
                link.query(adapter.commands.measure_source_ch1)
                raw = link.query(adapter.commands.measure_frequency_query)
                mqtt.publish(
                    f"{prefix}/measurements",
                    {
                        "ts": utc_now(),
                        "node": node_id,
                        "instrument": instrument,
                        "kind": "measurement_frequency",
                        "data": adapter.parse_scalar(raw),
                    },
                )
            except Exception as exc:
                mqtt.publish(
                    f"{prefix}/events",
                    {
                        "ts": utc_now(),
                        "node": node_id,
                        "instrument": instrument,
                        "kind": "error",
                        "data": {"stage": "poll", "error": str(exc)},
                    },
                )
            time.sleep(poll_interval)
    finally:
        mqtt.close()
        link.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
