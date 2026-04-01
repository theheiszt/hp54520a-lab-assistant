from __future__ import annotations
import json
from typing import Any, Dict
import paho.mqtt.client as mqtt


class MqttPublisher:
    def __init__(self, host: str, port: int, username: str, password: str) -> None:
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        if username:
            self.client.username_pw_set(username=username, password=password)
        self.client.connect(host, port, keepalive=30)
        self.client.loop_start()

    def publish(self, topic: str, message: Dict[str, Any]) -> None:
        self.client.publish(topic, json.dumps(message), qos=1, retain=False)

    def close(self) -> None:
        self.client.loop_stop()
        self.client.disconnect()
