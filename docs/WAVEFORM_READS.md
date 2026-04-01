# Waveform Read Notes

These notes capture the practical waveform-read behavior described in the HP 54520A / 54540 Series Programmer's Reference.

## Before reading waveform metadata

Before calling `:WAVeform:PREamble?`, the oscilloscope must either be stopped or a `:DIGitize ...` command must already have been executed.

## Suggested metadata sequence

1. `:SYSTem:HEADer OFF`
2. `:WAVeform:SOURce CHANnel1`
3. `:WAVeform:FORMat ASCii`
4. `:DIGitize CHANnel1`
5. `*OPC?`
6. `:WAVeform:PREamble?`
7. `:WAVeform:XINCrement?`
8. `:WAVeform:POINts?`

## Preamble field order

The waveform preamble returns these fields in order:

1. format
2. type
3. points
4. count
5. xincrement
6. xorigin
7. xreference
8. yincrement
9. yorigin
10. yreference

## Format values

- `0` = ASCII
- `1` = BYTE
- `2` = WORD
- `4` = COMPRESSED

## Type values

- `0` = INVALID
- `1` = normal / realtime
- `2` = average
- `3` = envelope
- `4` = rawdata
- `5` = peak detect

## Important query rule

Read every query result before sending the next program message. If you send another command before reading a pending response, the output buffer can be cleared and the current response can be lost.
