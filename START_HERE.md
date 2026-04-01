# Start Here

The root README already existed when this repository was created. This file is the current project entrypoint for the scaffold.

## What was added

- `docs/ARCHITECTURE.md`
- `docs/HARDWARE.md`
- `docs/ROADMAP.md`
- `docs/HP54520A_COMMANDS.md`
- `docs/RUN.md`
- `docs/NOTES.md`
- `udoo_node/` scaffold
- `pi_brain/` scaffold
- `.gitignore`
- `LICENSE`

## First task

Pick the actual GPIB adapter and replace the placeholder backend in `udoo_node/gpib_link.py`.

## First manual commands to prove

- `*IDN?`
- `*OPC?`
- `:MEASure:SOURce CHANnel1`
- `:MEASure:FREQuency?`

## Then move on to

- `:DIGitize CHANnel1`
- `:WAVeform:PREamble?`
