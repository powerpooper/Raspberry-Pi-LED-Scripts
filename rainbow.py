#!/usr/bin/python
# -*- coding: utf-8 -*-

import signal
import time
from neopixel import *
import sys, getopt
import os
from configparser import ConfigParser
import string
from varfile import *
import argparse

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=60):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbowCycle(strip, wait_ms=80, iterations=256):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def quit_gracefully(*args):
    filename = "/usr/lib/cgi-bin/varfile.py"
    varfile = open(filename, 'r')
    lines=varfile.readlines()
    result=lines[8]
    newcolor=result[9:-2]
    varfile.close()
    print newcolor

    if newcolor == 'red':
        colorWipe(strip, Color(255,0,0), 10)

    if newcolor == 'blue':
        colorWipe(strip, Color(0,0,255), 10)

    if newcolor == 'green':
        colorWipe(strip, Color(0,255,0), 10)

    if newcolor == 'white':
        colorWipe(strip, Color(255,255,255), 10)

    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, quit_gracefully)


    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    try:

        while 1:
            rainbowCycle(strip)
            pass
    except KeyboardInterrupt:
        if quit_gracefully():
            print("Done")
