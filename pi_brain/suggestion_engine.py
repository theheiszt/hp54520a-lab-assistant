from __future__ import annotations
from typing import Any, Dict, List


def suggest_next_steps(message: Dict[str, Any]) -> List[str]:
    suggestions: List[str] = []
    data = message.get("data", {})
    value = data.get("value") if isinstance(data, dict) else None

    if isinstance(value, (float, int)):
        if value < 10:
            suggestions.append(
                "Low-frequency reading. Increase timebase and inspect ripple or slow control behavior."
            )
        elif value > 1e6:
            suggestions.append(
                "High-frequency reading. Verify probe compensation, ground lead length, and acquisition settings."
            )

    if not suggestions:
        suggestions.append("Capture a waveform preamble and waveform data next.")
        suggestions.append(
            "Compare the measured node against the expected signal in the relevant datasheet."
        )

    return suggestions
