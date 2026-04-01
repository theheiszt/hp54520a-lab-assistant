# Backend Contract

Place adapter-specific GPIB transport implementations in this directory.

## Goal

Keep the project-level command and parsing logic independent from the physical controller implementation.

## Expected minimal interface

Each backend should support:

- `query(command: str) -> str`
- `close() -> None`

## Recommended flow

1. open controller connection
2. send one program message
3. read one response fully
4. return the decoded string to the caller

## Examples of future backend modules

- `linux_usb_gpib.py`
- `prologix_serial.py`
- `pyvisa_backend.py`

`udoo_node/gpib_link.py` should stay as the stable project-level wrapper.
