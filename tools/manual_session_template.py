from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


LOG_PATH = Path("manual_session_log.jsonl")


class ScopeTransport:
    """
    Replace this stub with the actual adapter-backed implementation.
    Expected surface area is intentionally tiny.
    """

    def query(self, command: str) -> str:
        raise NotImplementedError("Hook in your chosen GPIB adapter here.")


COMMANDS = [
    "*IDN?",
    "*OPC?",
    ":MEASure:SOURce CHANnel1",
    ":MEASure:FREQuency?",
    ":DIGitize CHANnel1",
    "*OPC?",
    ":WAVeform:SOURce CHANnel1",
    ":WAVeform:FORMat ASCii",
    ":WAVeform:PREamble?",
    ":WAVeform:XINCrement?",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def append_log(record: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


def main() -> int:
    transport = ScopeTransport()

    for command in COMMANDS:
        try:
            response = transport.query(command)
            append_log(
                {
                    "ts": utc_now(),
                    "command": command,
                    "response": response,
                }
            )
            print(f">> {command}")
            print(f"<< {response}")
        except Exception as exc:
            append_log(
                {
                    "ts": utc_now(),
                    "command": command,
                    "error": str(exc),
                }
            )
            print(f"!! {command}: {exc}")
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
