from __future__ import annotations
from collections import deque
from threading import Lock
from typing import Any, Deque, Dict, List


class StateStore:
    def __init__(self, max_items: int = 200) -> None:
        self._lock = Lock()
        self._messages: Deque[Dict[str, Any]] = deque(maxlen=max_items)

    def add(self, msg: Dict[str, Any]) -> None:
        with self._lock:
            self._messages.append(msg)

    def latest(self) -> Dict[str, Any] | None:
        with self._lock:
            return self._messages[-1] if self._messages else None

    def all(self) -> List[Dict[str, Any]]:
        with self._lock:
            return list(self._messages)
