from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class ScopeCommandSet:
    identity_query: str = "*IDN?"
    operation_complete_query: str = "*OPC?"
    header_off: str = ":SYSTem:HEADer OFF"
    longform_off: str = ":SYSTem:LONGform OFF"
    digitize_ch1: str = ":DIGitize CHANnel1"
    measure_source_ch1: str = ":MEASure:SOURce CHANnel1"
    measure_frequency_query: str = ":MEASure:FREQuency?"
    measure_risetime_query: str = ":MEASure:RISetime?"
    waveform_source_ch1: str = ":WAVeform:SOURce CHANnel1"
    waveform_format_ascii: str = ":WAVeform:FORMat ASCii"
    waveform_preamble_query: str = ":WAVeform:PREamble?"
    waveform_xincrement_query: str = ":WAVeform:XINCrement?"


class HP54520AAdapter:
    def __init__(self, command_set: Optional[ScopeCommandSet] = None) -> None:
        self.commands = command_set or ScopeCommandSet()

    def bootstrap_commands(self) -> list[str]:
        return [self.commands.header_off, self.commands.longform_off]

    def parse_identity(self, raw: str) -> Dict[str, Any]:
        raw = raw.strip()
        parts = [p.strip() for p in raw.split(",")] if raw else []
        parsed: Dict[str, Any] = {"raw": raw, "ok": bool(raw)}
        if len(parts) >= 4:
            parsed["vendor"] = parts[0]
            parsed["model"] = parts[1]
            parsed["serial"] = parts[2]
            parsed["revisions"] = parts[3:]
        return parsed

    def parse_scalar(self, raw: str) -> Dict[str, Any]:
        raw = raw.strip()
        try:
            return {"raw": raw, "value": float(raw)}
        except Exception:
            return {"raw": raw}

    def parse_preamble(self, raw: str) -> Dict[str, Any]:
        raw = raw.strip()
        parts = [p.strip() for p in raw.split(",")] if raw else []
        out: Dict[str, Any] = {"raw": raw, "fields": parts}
        if len(parts) >= 10:
            out["parsed"] = {
                "format": parts[0],
                "type": parts[1],
                "points": parts[2],
                "count": parts[3],
                "xincrement": parts[4],
                "xorigin": parts[5],
                "xreference": parts[6],
                "yincrement": parts[7],
                "yorigin": parts[8],
                "yreference": parts[9],
            }
        return out
