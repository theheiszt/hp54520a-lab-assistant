# Roadmap

## Phase 1 — Prove the transport

- [ ] connect the scope through a working GPIB adapter
- [ ] verify the scope address
- [ ] confirm `*IDN?`
- [ ] confirm `*OPC?`
- [ ] confirm `:MEASure:SOURce CHANnel1`
- [ ] confirm `:MEASure:FREQuency?`

## Phase 2 — Structured measurement ingest

- [ ] publish measurement responses over MQTT
- [ ] normalize numeric results into JSON
- [ ] expose `/scope/latest` and `/scope/history`

## Phase 3 — Waveform metadata path

- [ ] confirm `:DIGitize CHANnel1`
- [ ] confirm `:WAVeform:PREamble?`
- [ ] confirm waveform format handling
- [ ] capture preamble + waveform data as session artifacts

## Phase 4 — Lab assistant features

- [ ] microscope camera pipeline on Raspberry Pi
- [ ] OCR for chip/package markings
- [ ] datasheet candidate retrieval
- [ ] guided test suggestions based on live measurements

## Phase 5 — Maintenance workflows

- [ ] self-test checklist support
- [ ] calibration / service reminders
- [ ] issue logging and troubleshooting history

## Phase 6 — Safer agent layer

- [ ] wrap instrument actions in deterministic tools
- [ ] add reasoning over telemetry, OCR, and datasheet context
- [ ] keep all destructive or risky actions behind explicit human approval
