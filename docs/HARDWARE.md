# Hardware Planning

## Scope side

The HP 54520A family programmer's reference targets **HP-IB / GPIB (IEEE-488.2)** remote programming.

That means the practical command path should be:

- HP 54520A
- GPIB cable
- USB-to-GPIB adapter
- Linux host

## Linux host options

### Option A: Raspberry Pi 3B+
Use the Pi as both:

- instrument controller
- MQTT publisher
- AI / API host

This is the fastest way to get a first working system.

### Option B: UDOO Key + Raspberry Pi
Use the UDOO Key as the edge node and the Pi as the lab brain.

That gives you:

- one box for direct instrument control
- one box for microscope, OCR, data services, and AI workflows

## Recommended first milestone

Start with the simplest real hardware path:

1. Pi + USB-to-GPIB
2. prove command/query round-trip
3. prove measurement query
4. prove waveform preamble query
5. then move the driver layer to the UDOO if you still want wireless separation

## Why not RS-485

RS-485 modules are not relevant to the HP 54520A remote programming path described in the manuals.

## Why not raw AI control

Do not let a language model write arbitrary transport commands directly to the scope.
Use a small, deterministic command surface instead.
