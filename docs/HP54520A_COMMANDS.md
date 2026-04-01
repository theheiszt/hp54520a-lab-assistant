# HP 54520A Commands

## Safe bootstrap

- `:SYSTem:HEADer OFF`
- `:SYSTem:LONGform OFF`

## Identity / readiness

- `*IDN?`
- `*OPC?`

## Measurement path

- `:MEASure:SOURce CHANnel1`
- `:MEASure:FREQuency?`
- `:MEASure:RISetime?`

## Acquisition path

- `:DIGitize CHANnel1`

## Waveform path

- `:WAVeform:SOURce CHANnel1`
- `:WAVeform:FORMat ASCii`
- `:WAVeform:PREamble?`
- `:WAVeform:XINCrement?`

## Notes

- Read `:WAVeform:PREamble?` after the scope is stopped or after `:DIGitize ...` has already executed.
- Query responses in the programming reference terminate with newline.
- Keep the first integration narrow: identity, operation-complete, one measurement query, then waveform metadata.
