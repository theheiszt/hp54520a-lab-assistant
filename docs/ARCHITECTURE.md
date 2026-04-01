# Architecture Overview

## System split

The project is intentionally split into two layers:

1. **UDOO edge node**
2. **Raspberry Pi lab brain**

```text
HP 54520A -> GPIB cable -> USB-to-GPIB adapter -> Linux host
                                               |
                                            MQTT JSON
                                               |
                                        Raspberry Pi 3B+
```

## UDOO edge node responsibilities

- own the low-level instrument connection
- speak deterministic GPIB commands
- normalize raw replies into structured telemetry
- publish telemetry and events over MQTT
- avoid embedding any high-level AI behavior

## Raspberry Pi lab brain responsibilities

- ingest MQTT telemetry
- retain recent state and session history
- generate rule-based suggestions first
- expose an API for later agent orchestration
- integrate microscope vision, OCR, part lookup, and datasheet workflows

## Design rule

The AI layer should sit **above** a deterministic tool boundary.

Recommended control stack:

1. GPIB backend / adapter
2. typed scope operations
3. telemetry + storage
4. reasoning / agent suggestions

## Why this matters

This keeps the project:

- easier to debug
- safer around hardware
- easier to test offline
- ready for incremental expansion instead of a fragile all-at-once build
