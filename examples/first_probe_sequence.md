# First Manual Probe Sequence

Use this sequence before attempting any agent-driven workflow.

## Goal

Prove that the instrument link, message flow, and parser assumptions are sound.

## Step 1 — identity and readiness

- `*IDN?`
- `*OPC?`

Confirm the reply is stable and repeatable.

## Step 2 — simple scalar measurement

- `:MEASure:SOURce CHANnel1`
- `:MEASure:FREQuency?`

Capture the raw reply and the parsed float value.

## Step 3 — acquisition

- `:DIGitize CHANnel1`
- `*OPC?`

## Step 4 — waveform metadata

- `:WAVeform:SOURce CHANnel1`
- `:WAVeform:FORMat ASCii`
- `:WAVeform:PREamble?`
- `:WAVeform:XINCrement?`

## What to save

For each step, log:

- command sent
- raw response
- parsed response
- timestamp
- instrument address
- test conditions

That log becomes the baseline for the AI layer later.
