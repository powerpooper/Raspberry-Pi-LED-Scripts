#!/usr/bin/python
# -*- coding: utf-8 -*-

import signal
import time
import re
from neopixel import *
import sys, getopt
import os
from configparser import ConfigParser
import string
from varfile import *
import argparse
import math

file_name =  os.path.basename(sys.argv[0])
lightLevel = sys.argv[1]


def SetAll(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)

def getBrightPercentage():
        convert = (float(lightLevel)/100) * 255
	percentage = int(convert)
	with open("varfile.py") as f:
		for line in f:
			if "LED_BRIGHTNESS =" in line:
				curval=line
				s = open("varfile.py").read()
				s = s.replace('%s' % curval, "LED_BRIGHTNESS = " + str(percentage) + "\n")
				f = open("varfile.py", 'w')
				f.write(s)
				f.close()
	return int(percentage)
getBrightPercentage()

def updatePercentage():
        with open("varfile.py") as f:
                for line in f:
                        if "BrightPercent =" in line:
                                curval=line
                                s = open("varfile.py").read()
                                s = s.replace('%s' % curval, "BrightPercent = "'"' + sys.argv[1] + '"'"\n")
                                f = open("varfile.py", 'w')
                                f.write(s)
                                f.close()

# If the colornow is a HEX value, convert it to RGB
def hexLastRGB(lastcolor):
        lastcolorhex = lastcolor.lstrip('#')
        hlen = len(lastcolorhex)
        return tuple(int(lastcolorhex[i:i+hlen/3], 16) for i in range(0, hlen, hlen/3))

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=5):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def colorBright():
	for i in range (206):
		strip.setPixelColor(i, bakcolor)
	strip.show()


if Power == "on":
	# Getting the color and adjusting brightness variables
	lastcolornum = hexLastRGB(lastcolor)
	bakcolor = Color(lastcolornum[0], lastcolornum[1], lastcolornum[2])
	LED_BRIGHTNESS = getBrightPercentage()
	updatePercentage()


	if __name__ == '__main__':
		# Create NeoPixel object with appropriate configuration.
		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
		# Intialize the library (must be called once before other functions).
		strip.begin()
		colorBright()
		exit()

