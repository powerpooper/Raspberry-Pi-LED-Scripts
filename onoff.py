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
import psutil

file_name =  os.path.basename(sys.argv[0])
onoff = sys.argv[1]

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Update varfile.py
def updateOther():
        with open("varfile.py") as f:
                for line in f:
                        if "lastcolor =" in line:
                                curval=line
                                s = open("varfile.py").read()
                                s = s.replace('%s' % curval, "lastcolor = "'"#' + colornow + '"'"\n")
                                f = open("varfile.py", 'w')
                                f.write(s)
                                f.close()

def updateOnOff():
        with open("varfile.py") as f:
                for line in f:
                        if "Power =" in line:
                                curval=line
                                s = open("varfile.py").read()
                                s = s.replace('%s' % curval, "Power = "'"' + onoff + '"'"\n")
                                f = open("varfile.py", 'w')
                                f.write(s)
                                f.close()

# If the colornow is a HEX value, convert it to RGB
def hexLastRGB(lastcolor):
        lastcolorhex = lastcolor.lstrip('#')
        hlen = len(lastcolorhex)
        return tuple(int(lastcolorhex[i:i+hlen/3], 16) for i in range(0, hlen, hlen/3))

def colorWipe(strip, color, wait_ms=60):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def wheelOnColor(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos > 206:
        return oncolor
    elif pos > 206:
        pos += 0
        return red
    else:
        pos -= 0
        return Color(0, 0, 0)

def colorWipeOn(strip, wait_ms=10, iterations=208):
    """Wipe color across display a pixel at a time."""
    for j in range(iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheelOnColor((i+j)));
        strip.show()
        time.sleep(wait_ms/1000.0)

def wheelOffColor(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 0:
        return Color(0, 0, 0)
    elif pos < 1:
        pos -= 2
        return Color(0, 0, 0)
    else:
        pos -= 96
        return oncolor


def colorWipeOff(strip, wait_ms=10, iterations=208):
    """Wipe color across display a pixel at a time."""
    for j in range(iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheelOffColor((i-j)));
        strip.show()
        time.sleep(wait_ms/1000.0)

lastcolornum = hexLastRGB(lastcolor)
oncolor = Color(lastcolornum[0], lastcolornum[1], lastcolornum[2])

def led_power():
	if Power == "off":
		if onoff == "on":
			colorWipeOn(strip)

	if Power == "on":
		if onoff == "off":
			colorWipeOff(strip)

	# Update Power variable
	updateOnOff()

# Here we go!
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	while True:
		animationpid = psutil.pid_exists(Animation)

		if animationpid in [False]:
			break

		time.sleep(0.1)

	led_power()

	exit()
