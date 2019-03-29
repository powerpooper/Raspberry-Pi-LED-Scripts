#This is the function library.  This is imported by main.py

from configparser import ConfigParser
from neopixel import *
from array import *
from varfile import *
import time
import math
import random
import argparse
import signal
import sys
import datetime
import getopt
import os
import string
import subprocess
import re
import fileinput
import gc

LED_STRIP = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


#Define functions which animate LEDs in various ways.
def SetAll(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)


#################### 						####################
#################### 		Halloween Funvtions		####################
#################### 		       Start			####################
#################### 						####################

def NewKitt(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    RightToLeft(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    LeftToRight(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    OutsideToCenter(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    CenterToOutside(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    RightToLeft(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    LeftToRight(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    OutsideToCenter(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)
    CenterToOutside(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay)

#Used by NewKitt
def CenterToOutside(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(int(math.floor((LED_COUNT-EyeSize)/2)), 0, -1):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.setPixelColor(LED_COUNT - i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(LED_COUNT - i - j, Color(red, green, blue))
        strip.setPixelColor(LED_COUNT - i - EyeSize - 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

#Used by NewKitt
def OutsideToCenter(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(0, int(math.floor((LED_COUNT-EyeSize)/2))):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.setPixelColor(LED_COUNT - i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(LED_COUNT - i - j, Color(red, green, blue))
        strip.setPixelColor(LED_COUNT - i - EyeSize - 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

#Used by NewKitt
def LeftToRight(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(0, LED_COUNT - EyeSize - 2):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize+1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

#Used by NewKitt
def RightToLeft(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    for i in range(LED_COUNT - EyeSize - 2, 0, -1):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        for j in range(1, EyeSize + 1):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red/10)), int(math.floor(green/10)), int(math.floor(blue/10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

def RunningLightsSnakeReverse(strip, red, green, blue, WaveDelay):
    Position=0
    for i in range (0, (LED_COUNT * 2)):
        Position = Position + 20
        for i in range (0, LED_COUNT):
            strip.setPixelColor(i, Color(int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * red)), int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * green)), int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * blue))))
            Position = Position + 5
        strip.show()
        time.sleep(WaveDelay/100.0)

def FillDownOrangeReverse(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(0, 0, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +41):
		for j in range(LED_COUNT+41, i+40, -1):
			strip.setPixelColor(j-41, Color(255, 60, 0))
			if j<206:
				strip.setPixelColor(j+1, Color(0, 0, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def FillDownGreenReverse(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(0, 0, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +41):
		for j in range(LED_COUNT+41, i+40, -1):
			strip.setPixelColor(j-41, Color(50, 140, 0))
			if j<206:
				strip.setPixelColor(j+1, Color(0, 0, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def FillDownRedReverse(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(0, 0, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +41):
		for j in range(LED_COUNT+41, i+40, -1):
			strip.setPixelColor(j-41, Color(255, 4, 0))
			if j<206:
				strip.setPixelColor(j+1, Color(0, 0, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def FillDownPurpleReverse(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(0, 0, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +41):
		for j in range(LED_COUNT+41, i+40, -1):
			strip.setPixelColor(j-41, Color(200, 0, 45))
			if j<206:
				strip.setPixelColor(j+1, Color(0, 0, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

#################### 						####################
#################### 		Halloween Funvtions		####################
#################### 		       	End			####################
#################### 						####################











#################### 						####################
#################### 		Christmas Funvtions		####################
#################### 		       Start			####################
#################### 						####################

def FillDownBlue(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(255, 147, 41))
        #Fill down with random colors
        for i in range(0, LED_COUNT, +4):
                for j in range(0,LED_COUNT-(i-2)):
			if i % 2 == 0:
				strip.setPixelColor(j-1, Color(255, 147, 41))
			if j>0:
				strip.setPixelColor(j+2, Color(0, 0, 255))
                        strip.show()
                        time.sleep(SpeedDelay)
                time.sleep(DisplayDelay)
        time.sleep(PauseDelay)

def ChristmasChaseBlue(strip, red, green, blue, SpeedDelay, Iterations):
        for i in range(0, Iterations):
                for j in range(0, 4):
                        for k in range(0, LED_COUNT, 4):
                                strip.setPixelColor(k + j, Color(red, green, blue))
                        strip.show()
                        time.sleep(SpeedDelay)
                        for k in range(0, LED_COUNT, 4):
                                strip.setPixelColor(k + j, Color(0, 0, 255))

def SnowSparkle(strip, red, green, blue, SparkleDelay, SpeedDelay):
    SetAll(strip, Color(red, green, blue))
    pixel=random.randrange(0, LED_COUNT)
    strip.setPixelColor(pixel, Color(255, 255, 255))
    strip.show()
    time.sleep(SparkleDelay)
    strip.setPixelColor(pixel, Color(red, green, blue))
    strip.show()
    time.sleep(SpeedDelay)

def EveryOtherRed(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
        #Fill down with random colors
        for i in range(0, LED_COUNT, +2):
                if i>0:
                        if i % 1 == 0:
                                strip.setPixelColor(i-1, Color(255, 0, 0))
                        if i % 2 == 0:
                                strip.setPixelColor(i, Color(255, 147, 41))
                strip.show()
                time.sleep(SpeedDelay)
                time.sleep(DisplayDelay)
        time.sleep(PauseDelay)

def ChristmasChaseRed(strip, red, green, blue, SpeedDelay, Iterations):
        for i in range(0, Iterations):
                for j in range(0, 2):
			for k in range(0, LED_COUNT, 2):
				strip.setPixelColor(k + j + 3, Color(red, green, blue))
			strip.show()
			time.sleep(SpeedDelay)
			for k in range(0, LED_COUNT, 2):
				strip.setPixelColor(k + j + 1, Color(255, 147, 41))

#################### 						####################
#################### 		Christmas Funvtions		####################
#################### 		       	End			####################
#################### 						####################


"""
Done
"""
