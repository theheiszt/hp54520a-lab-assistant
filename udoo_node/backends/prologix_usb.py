from __future__ import annotations

import time
from typing import Optional

import serial


class PrologixUsbBackend:
    """
    First concrete GPIB backend stub for the project.

    This backend targets a Prologix GPIB-USB controller exposed as a virtual
    serial port on Linux.

    Scope of this first version:
    - good for controller bring-up
    - good for ASCII/scalar queries such as *IDN? and :MEASure:FREQuency?
    - intentionally conservative for waveform/binary reads
    """

    def __init__(
        self,
        port: str,
        gpib_address: int,
        baudrate: int = 115200,
        serial_timeout_sec: float = 0.5,
        write_timeout_sec: float = 1.0,
        read_tmo_ms: int = 3000,
        settle_delay_sec: float = 0.05,
    ) -> None:
        self.port = port
        self.gpib_address = gpib_address
        self.read_tmo_ms = read_tmo_ms
        self.settle_delay_sec = settle_delay_sec
        self.ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=serial_timeout_sec,
            write_timeout=write_timeout_sec,
        )
        self._configure_controller()

    def _write_line(self, line: str) -> None:
        self.ser.write((line + "\n").encode("ascii", errors="ignore"))
        self.ser.flush()

    def _read_available(self) -> bytes:
        data = bytearray()
        while True:
            chunk = self.ser.read(4096)
            if not chunk:
                break
            data.extend(chunk)
            if len(chunk) < 4096:
                break
        return bytes(data)

    def _configure_controller(self) -> None:
        self.ser.reset_input_buffer()
        self._write_line("++mode 1")
        self._write_line(f"++addr {self.gpib_address}")
        self._write_line("++auto 0")
        self._write_line(f"++read_tmo_ms {self.read_tmo_ms}")
        time.sleep(self.settle_delay_sec)
        self.ser.reset_input_buffer()

    def set_address(self, gpib_address: int) -> None:
        self.gpib_address = gpib_address
        self._write_line(f"++addr {gpib_address}")

    def controller_version(self) -> str:
        self.ser.reset_input_buffer()
        self._write_line("++ver")
        time.sleep(self.settle_delay_sec)
        return self._read_available().decode("ascii", errors="replace").strip()

    def write(self, command: str) -> None:
        self.ser.reset_input_buffer()
        self._write_line(command)

    def query_bytes(self, command: str) -> bytes:
        self.ser.reset_input_buffer()
        self._write_line(command)
        self._write_line("++read eoi")
        time.sleep(self.settle_delay_sec)
        return self._read_available()

    def query(self, command: str) -> str:
        raw = self.query_bytes(command)
        return raw.decode("ascii", errors="replace").strip()

    def close(self) -> None:
        if self.ser and self.ser.is_open:
            self.ser.close()
