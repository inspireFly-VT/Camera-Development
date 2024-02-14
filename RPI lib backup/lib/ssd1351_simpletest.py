# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""

import board
import busio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_ssd1351 import SSD1351

# Release any resources currently in use for the displays
displayio.release_displays()

spi = busio.SPI(clock=board.GP18, MOSI=board.GP19, MISO=board.GP16)
tft_cs = board.GP21
tft_dc = board.GP14

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.GP7, baudrate=16000000
)

display = SSD1351(display_bus, width=128, height=128)

# Make the display context
splash = displayio.Group()
display.root_group = splash

# Load .bmp image
bmp = displayio.OnDiskBitmap(open("inspireFly_Lab.bmp", "rb"))

# Create a TileGrid to display the .bmp image
bg_sprite = displayio.TileGrid(bmp, pixel_shader=displayio.ColorConverter(), x=0, y=0)
splash.append(bg_sprite)


while True:
    pass
