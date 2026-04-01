# GPIB Adapter Options

The current repository intentionally leaves the low-level GPIB implementation open because the correct backend depends on the hardware you end up using.

## Good selection criteria

- Linux support on Raspberry Pi 3B+ or UDOO Key
- stable query/write behavior for IEEE-488.2 instruments
- access to bus addressing and termination settings
- enough community examples to debug bring-up quickly

## Integration rule

Keep the adapter-specific logic isolated inside `udoo_node/gpib_link.py` or a backend module imported from there.

The rest of the project should continue to call a small deterministic interface:

- `query(command: str) -> str`
- `close() -> None`

## First prove-out sequence

1. connect the physical GPIB controller
2. verify the instrument address
3. send `*IDN?`
4. send `*OPC?`
5. send `:MEASure:SOURce CHANnel1`
6. send `:MEASure:FREQuency?`

Only after those work should you move on to waveform reads.
