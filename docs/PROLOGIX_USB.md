# Prologix GPIB-USB Backend

The first concrete backend choice for this project is the Prologix GPIB-USB controller.

## Why this is the first backend

- it presents as a virtual serial port on Linux
- it does not force the project into a heavyweight vendor-specific driver stack
- it is a practical fit for Raspberry Pi and Linux-based bring-up

## Controller command model used by this backend

This backend uses the controller-side command flow below:

1. `++mode 1`
2. `++addr <instrument address>`
3. `++auto 0`
4. `++read_tmo_ms <milliseconds>`
5. instrument command such as `*IDN?`
6. `++read eoi`

## Why `++auto 0`

Using explicit reads is safer for mixed command/query sessions.
It avoids the common pattern where a non-query command is followed by an automatic read and the instrument reports a query-unterminated style error.

## Good first commands

- `*IDN?`
- `*OPC?`
- `:MEASure:SOURce CHANnel1`
- `:MEASure:FREQuency?`

## Current limitation

The backend is intentionally conservative and aimed at ASCII/scalar queries first.
Waveform and binary transfer support should be extended after the basic command path is proven stable.
