# UDOO Edge Node

This directory contains the low-level instrument side of the project.

## Responsibilities

- connect to the HP 54520A over GPIB
- issue deterministic commands
- normalize replies into structured JSON
- publish updates over MQTT

## Current limitation

`gpib_link.py` still contains a placeholder backend. Replace it with the adapter-specific Linux implementation once the hardware interface is chosen.

## Run

```bash
python main.py
```
