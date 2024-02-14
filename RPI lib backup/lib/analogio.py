# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`analogio` - Analog input and output control
============================================
See `CircuitPython:analogio` in CircuitPython for more details.
Not supported by all boards.

* Author(s): Carter Nelson, Melissa LeBlanc-Williams
"""

import sys

from adafruit_blinka.agnostic import detector

# pylint: disable=ungrouped-imports,wrong-import-position,unused-import

if detector.board.microchip_mcp2221:
    from adafruit_blinka.microcontroller.mcp2221.analogio import AnalogIn
    from adafruit_blinka.microcontroller.mcp2221.analogio import AnalogOut
elif detector.board.greatfet_one:
    from adafruit_blinka.microcontroller.nxp_lpc4330.analogio import AnalogIn
    from adafruit_blinka.microcontroller.nxp_lpc4330.analogio import AnalogOut
elif detector.board.any_odroid_40_pin:
    from adafruit_blinka.microcontroller.generic_linux.sysfs_analogin import AnalogIn
elif detector.board.any_siemens