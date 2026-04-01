# Quick Run Guide

## Bring-up sequence

1. Connect the scope through a supported GPIB controller.
2. Confirm the scope GPIB address.
3. Prove these commands manually:
   - `*IDN?`
   - `*OPC?`
   - `:MEASure:SOURce CHANnel1`
   - `:MEASure:FREQuency?`
4. Then test:
   - `:DIGitize CHANnel1`
   - `:WAVeform:SOURce CHANnel1`
   - `:WAVeform:FORMat ASCii`
   - `:WAVeform:PREamble?`

## Edge node

```bash
cd udoo_node
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Pi brain

```bash
cd pi_brain
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn api_main:app --host 0.0.0.0 --port 8000
```

## API endpoints

- `/health`
- `/scope/latest`
- `/scope/history`
- `/scope/suggestions`

## Current limitation

The GPIB backend is still a placeholder. Replace it with the adapter-specific backend once the hardware choice is finalized.
