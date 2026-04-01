from __future__ import annotations
from typing import Protocol


class QueryBackend(Protocol):
    def query(self, command: str) -> str: ...
    def close(self) -> None: ...


class ManualPlaceholderGpibBackend:
    def __init__(
        self,
        resource: str,
        read_termination: str = "\n",
        write_termination: str = "\n",
        timeout_ms: int = 3000,
    ) -> None:
        self.resource = resource
        self.read_termination = read_termination
        self.write_termination = write_termination
        self.timeout_ms = timeout_ms

    def query(self, command: str) -> str:
        raise NotImplementedError(
            "Hook your Linux GPIB adapter here. Start by testing '*IDN?' and ':MEAS:FREQ?'."
        )

    def close(self) -> None:
        return


class GpibScopeLink:
    def __init__(
        self,
        backend: str,
        resource: str,
        read_termination: str = "\n",
        write_termination: str = "\n",
        timeout_ms: int = 3000,
    ) -> None:
        if backend.lower() != "manual_placeholder":
            raise ValueError(f"Unsupported backend: {backend}")
        self.backend: QueryBackend = ManualPlaceholderGpibBackend(
            resource=resource,
            read_termination=read_termination,
            write_termination=write_termination,
            timeout_ms=timeout_ms,
        )

    def query(self, command: str) -> str:
        return self.backend.query(command)

    def close(self) -> None:
        self.backend.close()
