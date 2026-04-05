# HP 54520A Lab Assistant

A split-edge lab automation project for collecting measurements from an **HP 54520A oscilloscope** and turning them into structured telemetry and actionable suggestions.

## Project goals

- Keep hardware control deterministic and debuggable.
- Publish normalized scope telemetry over MQTT.
- Build a higher-level "lab brain" service for state, history, and suggestions.
- Leave room for future agent workflows (vision, OCR, parts lookup, datasheets) above a stable tool boundary.

## Architecture

```text
HP 54520A -> GPIB cable -> USB-to-GPIB adapter -> Linux host (UDOO node)
                                                          |
                                                       MQTT JSON
                                                          |
                                              Raspberry Pi 3B+ (lab brain)
```

### Components

- **`udoo_node/`**
  - owns scope/GPIB communication
  - executes typed scope commands
  - parses scope replies into structured values
  - publishes telemetry/events to MQTT

- **`pi_brain/`**
  - ingests MQTT telemetry
  - stores current + recent scope state
  - serves API endpoints for latest state/history/suggestions
  - runs rule-based suggestion logic as a foundation for later AI orchestration

## Repository layout

- `docs/ARCHITECTURE.md` – system split and design rationale
- `docs/RUN.md` – bring-up and local run commands
- `docs/HARDWARE.md` – hardware integration notes
- `docs/HP54520A_COMMANDS.md` – command reference notes
- `udoo_node/` – edge node implementation
- `pi_brain/` – Raspberry Pi API + suggestion engine
- `tests/` – unit tests

## Quick start

### 1) Validate hardware command path

After wiring the scope and adapter, manually validate:

- `*IDN?`
- `*OPC?`
- `:MEASure:SOURce CHANnel1`
- `:MEASure:FREQuency?`

Then validate waveform flow:

- `:DIGitize CHANnel1`
- `:WAVeform:SOURce CHANnel1`
- `:WAVeform:FORMat ASCii`
- `:WAVeform:PREamble?`

### 2) Run the edge node

```bash
cd udoo_node
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### 3) Run the lab brain API

```bash
cd pi_brain
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api_main:app --host 0.0.0.0 --port 8000
```

### 4) Run tests

```bash
pytest -q
```

## Current status / limitation

The base project scaffold is in place. Depending on your GPIB hardware choice, you may still need to finalize adapter-specific backend implementation and configuration before full end-to-end operation.

## Additional docs

Start with:

- `START_HERE.md`
- `docs/ARCHITECTURE.md`
- `docs/RUN.md`
