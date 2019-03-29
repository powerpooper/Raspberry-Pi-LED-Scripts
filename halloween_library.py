#This is the function library.  This is imported by main.py

import time
import math
import random
from neopixel import *
from array import *
import argparse
import signal
import sys
import datetime
import string
import subprocess
import re
import fileinput



#LED strip configuration:
LED_COUNT      = 96      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 20     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


#Define functions which animate LEDs in various ways.
def SetAll(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)

def FadeRGB(strip):
    for i in range(0, 3):
        #Fade In.
        for j in range (0, 256):
            if i == 0:
                SetAll(strip, Color(j, 0, 0))
            elif i == 1:
                SetAll(strip, Color(0, j, 0))
            elif i == 2:
                SetAll(strip, Color(0, 0, j))
            strip.show()
        #Fade Out.
        for j in range (256, 0, -1):
            if i == 0:
                SetAll(strip, Color(j, 0, 0))
            elif i == 1:
                SetAll(strip, Color(0, j, 0))
            elif i == 2:
                SetAll(strip, Color(0, 0, j))
            strip.show()

def FadeInOut(strip, red, green, blue):
    #Fade In.
    for i in range (0, 256):
        r = int(math.floor((i / 256.0) * red))
        g = int(math.floor((i / 256.0) * green))
        b = int(math.floor((i / 256.0) * blue))
        SetAll(strip, Color(r, g, b))
        strip.show()
    #Fade Out.
    for i in range (256, 0, -1):
        r = int(math.floor((i / 256.0) * red))
        g = int(math.floor((i / 256.0) * green))
        b = int(math.floor((i / 256.0) * blue))
        SetAll(strip, Color(r, g, b))
        strip.show()

def Cylon(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    for i in range (0, (LED_COUNT - EyeSize - 2)):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        for j in range(1, (EyeSize + 1)):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)
    for i in range ((LED_COUNT - EyeSize - 2), 0, -1):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        for j in range(1, (EyeSize + 1)):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)

def Twinkle(strip, red, green, blue, Count, SpeedDelay, OnlyOne):
    SetAll(strip, Color(0, 0, 0))
    for i in range (0, Count):
        strip.setPixelColor(random.randrange(0, LED_COUNT), Color(red, green, blue))
        strip.show()
        time.sleep(SpeedDelay)
        if OnlyOne:
            SetAll(strip, Color(0, 0, 0))
    time.sleep(SpeedDelay)

def TwinkleRandom(strip, Count, SpeedDelay, OnlyOne):
    SetAll(strip, Color(0, 0, 0))
    for i in range (0, Count):
        strip.setPixelColor(random.randrange(0, LED_COUNT), Color(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))
        strip.show()
        time.sleep(SpeedDelay)
        if OnlyOne:
            SetAll(strip, Color(0, 0, 0))
    time.sleep(SpeedDelay)

def Sparkle(strip, red, green, blue, SpeedDelay):
    pixel=random.randrange(0, LED_COUNT)
    strip.setPixelColor(pixel, Color(red, green, blue))
    strip.show()
    time.sleep(SpeedDelay)
    strip.setPixelColor(pixel, Color(0, 0, 0))

def SnowSparkle(strip, red, green, blue, SparkleDelay, SpeedDelay):
    SetAll(strip, Color(red, green, blue))
    pixel=random.randrange(0, LED_COUNT)
    strip.setPixelColor(pixel, Color(255, 255, 255))
    strip.show()
    time.sleep(SparkleDelay)
    strip.setPixelColor(pixel, Color(red, green, blue))
    strip.show()
    time.sleep(SpeedDelay)

def RunningLights(strip, red, green, blue, WaveDelay):
    Position=0
    for i in range (0, (LED_COUNT * 2)):
        Position = Position + 1
        for i in range (0, LED_COUNT):
            strip.setPixelColor(i, Color(int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * red)), int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * green)), int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * blue))))
        strip.show()
        time.sleep(WaveDelay)

def RunningLightsOther(strip, red, green, blue, WaveDelay):
    Position=0
    for i in range ((LED_COUNT * 2), 0, -1):
        Position = Position - 1
        for i in range (0, LED_COUNT):
            strip.setPixelColor(i, Color(int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * red)), int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * green)), int(math.floor(((math.sin(i+Position) * 127 + 128) / 255) * blue))))
        strip.show()
        time.sleep(WaveDelay)

def ColorWipe(strip, red, green, blue, SpeedDelay, PauseDelay):
	for i in range (0, LED_COUNT):
		strip.setPixelColor(i, Color(red, green, blue))
		strip.show()
		time.sleep(SpeedDelay)
	time.sleep(PauseDelay)

def ColorWipeReverse(strip, red, green, blue, SpeedDelay, PauseDelay):
	for i in range (LED_COUNT, 0, -1):
		strip.setPixelColor(i, Color(red, green, blue))
		strip.show()
		time.sleep(SpeedDelay)
	time.sleep(PauseDelay)

def Wheel(WheelPosition):
	#Generate rainbow colors across 0-255 positions.
	if WheelPosition < 85:
		return Color(WheelPosition * 3, 255 - WheelPosition * 3, 0)
	elif WheelPosition < 170:
		WheelPosition -= 85
		return Color(255 - WheelPosition * 3, 0, WheelPosition * 3)
	else:
		WheelPosition -= 170
		return Color(0, WheelPosition * 3, 255 - WheelPosition * 3)

def Rainbow(strip, SpeedDelay):
    for i in range(0, 256):
	for j in range(0, LED_COUNT):
		strip.setPixelColor(j, Wheel((j + i) & 255))
	strip.show()
	time.sleep(SpeedDelay)

def RainbowCycle(strip, Iterations, SpeedDelay):
    for i in range (0, 256 * Iterations):
        for j in range (0, LED_COUNT):
            strip.setPixelColor(j, Wheel((int(j * 256 / LED_COUNT) + i) & 255))
	strip.show()
	time.sleep(SpeedDelay)

def ColorChase(strip, red, green, blue, SpeedDelay):
	for i in range(LED_COUNT):
		strip.setPixelColor(i, Color(red, green, blue))
		strip.show()
		time.sleep(SpeedDelay)
		strip.setPixelColor(i, Color(0, 0, 0))
		strip.show()

def ColorChaseReverse(strip, red, green, blue, SpeedDelay):
	for i in range(LED_COUNT, 0, -1):
		strip.setPixelColor(i, Color(red, green, blue))
		strip.show()
		time.sleep(SpeedDelay)
		strip.setPixelColor(i, Color(0, 0, 0))
		strip.show()

def TheaterChase(strip, red, green, blue, SpeedDelay, Iterations):
	for i in range(0, Iterations):
		for j in range(0, 3):
			for k in range(0, LED_COUNT, 3):
				strip.setPixelColor(k + j, Color(red, green, blue))
			strip.show()
			time.sleep(SpeedDelay)
			for k in range(0, LED_COUNT, 3):
				strip.setPixelColor(k + j, Color(0, 0, 0))

def TheaterChaseRainbow(strip, SpeedDelay):
	#Rainbow movie theater light style chaser animation.
	for i in range(256):
		for j in range(3):
			for k in range(0, strip.numPixels(), 3):
				strip.setPixelColor(k + j, Wheel((k + i) % 255))
			strip.show()
			time.sleep(SpeedDelay)
			for k in range(0, strip.numPixels(), 3):
				strip.setPixelColor(k + j, Color(0, 0, 0))

def MeteorRain(strip, red, green, blue, MeteorSize, MeteorTrailDecay, MeteorRandomDecay, SpeedDelay):
    SetAll(strip, Color(0, 0, 0))
    for i in range (0, LED_COUNT + LED_COUNT):
        # Fade brightness all LEDs one step
        for j in range (0, LED_COUNT):
            if ((not MeteorRandomDecay) or ((random.randint(0, 10)>5))):
                FadeToBlack(strip, j, MeteorTrailDecay)
        # Draw meteor
        for j in range (0, MeteorSize):
            if (((i - j) < LED_COUNT) and ((i - j) >= 0)):
                strip.setPixelColor(i - j, Color(red, green, blue))
        strip.show()
        time.sleep(SpeedDelay)


#Used by MeteorRain
def FadeToBlack(strip, Position, FadeValue):
    OldColor = strip.getPixelColor(Position)
    r = (OldColor & 0x00ff0000) >> 16
    g = (OldColor & 0x0000ff00) >> 8
    b = (OldColor & 0x000000ff)
    if (r<=10):
        r = 0;
    else:
        r = r - (r * FadeValue / 256)
    if (g<=10):
        g = 0;
    else:
        g = g - (g * FadeValue / 256)
    if (b<=10):
        b = 0;
    else:
        b = b - (b * FadeValue / 256)
    strip.setPixelColor(Position, Color(r, g, b))

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

#The Heat array needs to be declaired globally.  You can put it in the main section (but not in the While loop), but not in the Fire function...
Heat = [0] * LED_COUNT
def Fire(strip, Heat, Cooling, Sparking, SpeedDelay):
    #Step 1.  Cool down every cell a little
    for i in range(0, LED_COUNT):
        CoolDown = random.randint(0, (int(math.floor((Cooling * 10) / LED_COUNT)) + 2))
        if (CoolDown > Heat[i]):
            Heat[i] = 0
        else:
            Heat[i] = Heat[i] - CoolDown
    #Step 2.  Heat from each cell drifts 'up' and diffuses a little
    for i in range((LED_COUNT - 1), 2, -1):
        Heat[i] = int(math.floor((Heat[i - 1] + Heat[i - 2] + Heat[i - 2]) / 3))
    #Step 3.  Randomly ignite new 'sparks' near the bottom
    if (random.randint(0, 255) < Sparking):
        y=random.randint(0, 7)
        #There are 2 different ways to do this part, the commented out line is the alternate
        Heat[y] = Heat[y] + random.randrange(160, 255)
        #Added check to original code so that the heat never exceeds 255
        if (Heat[y]>255): Heat[y]=255
        #Heat[y] = random.randrange(160, 255)
    #Step 4.  Convert heat to LED colors
    for i in range(0, LED_COUNT):
        SetPixelHeatColor(strip, i, Heat[i])
    #Step 5.  Display
    strip.show()
    time.sleep(SpeedDelay)

#Used by Fire
def SetPixelHeatColor(strip, Pixel, Temperature):
    #Scale 'heat' down from 0-255 to 0-191
    t192 = int(math.floor((Temperature / 255.0) * 191))
    #calculate ramp up from
    HeatRamp = t192 & 0x3F #0..63
    HeatRamp <<= 2 #scale up to 0..252
    #figure out which third of the spectrum we're in:
    if (t192 > 0x80):
        strip.setPixelColor(Pixel, Color(255, 255, HeatRamp))
    elif(t192 > 0x40):
        strip.setPixelColor(Pixel, Color(255, HeatRamp, 0))
    else:
        strip.setPixelColor(Pixel, Color(HeatRamp, 0, 0))

def HalloweenEyes(strip, red, green, blue, EyeWidth, EyeSpace, Fade, Steps, FadeDelay, EndPause):
    StartPoint = random.randint(0, LED_COUNT - (2 * EyeWidth) - EyeSpace)
    Start2ndEye = StartPoint + EyeWidth + EyeSpace
    for i in range(0, EyeWidth):
        strip.setPixelColor(StartPoint + i, Color(red, green, blue))
        strip.setPixelColor(Start2ndEye + i, Color(red, green, blue))
    strip.show()
    if (Fade):
        for i in range(Steps, -1, -1):
            r = i * int(math.floor(red / Steps))
            g = i * int(math.floor(green / Steps))
            b = i * int(math.floor(blue / Steps))
            for j in range(0, EyeWidth):
                strip.setPixelColor(StartPoint, Color(r, g, b))
                strip.setPixelColor(Start2ndEye, Color(r, g, b))
            strip.show()
            time.sleep(FadeDelay)
    SetAll(strip, Color(0, 0, 0))
    time.sleep(EndPause)

def RandomColors(strip, SpeedDelay):
    SetAll(strip, Color(0, 0, 0))
    while True:
        for i in range(0, LED_COUNT):
            r=random.randint(0, 255)
            g=random.randint(0, 255)
            b=random.randint(0, 255)
            strip.setPixelColor(i, Color(r, g, b))
        strip.show()
        time.sleep(SpeedDelay)

def FillDownOrange(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(0, 0, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT):
		for j in range(0,LED_COUNT-i):
			strip.setPixelColor(j, Color(255, 60, 0))
			if j>0:
				strip.setPixelColor(j-1, Color(0, 0, 0))
			strip.show()
            		time.sleep(SpeedDelay)
        	time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def FillDownOrangeReverse(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(0, 0, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +8):
		for j in range(LED_COUNT+8, i+7, -1):
			strip.setPixelColor(j-8, Color(255, 60, 0))
			if j<96:
				strip.setPixelColor(j+1, Color(0, 0, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def FillDownOrangeReverseOff(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
        SetAll(strip, Color(255, 60, 0))
        #Fill down with random colors
        for i in range(0, LED_COUNT, +5 ):
                for j in range(LED_COUNT+5, i+4, -1):
                        strip.setPixelColor(j-5, Color(0, 0, 0))
                        if j<96:
                                strip.setPixelColor(j+1, Color(255, 60, 0))
                        strip.show()
                        time.sleep(SpeedDelay)
                time.sleep(DisplayDelay)
        time.sleep(PauseDelay)

def FillDownOrangeOff(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(255, 60, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +4):
		for j in range(0,LED_COUNT-(i+2)):
			strip.setPixelColor(j, Color(0, 0, 0))
			if j>0:
				strip.setPixelColor(j-4, Color(255, 60, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def BurnOutOrange(strip, red, green, blue, MeteorSize, MeteorTrailDecay, MeteorRandomDecay, SpeedDelay):
	SetAll(strip, Color(255, 60, 0))
	for i in range (0, LED_COUNT + LED_COUNT):
	# Fade brightness all LEDs one step
		for j in range (0, LED_COUNT):
			if ((not MeteorRandomDecay) or ((random.randint(0, 10)>5))):
				FadeToBlack(strip, j, MeteorTrailDecay)
		strip.show()
		time.sleep(SpeedDelay)

def FillDownGreen(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(100, 2, 50))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +5):
		for j in range(0,LED_COUNT-i):
			strip.setPixelColor(j, Color(50, 140, 0))
			if j>0:
				strip.setPixelColor(j-5, Color(100, 2, 50))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def FillDownGreenReverse(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(0, 0, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +8):
		for j in range(LED_COUNT+8, i+7, -1):
			strip.setPixelColor(j-8, Color(50, 140, 0))
			if j<96:
				strip.setPixelColor(j+1, Color(0, 0, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def FillDownGreenReverseOff(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
        SetAll(strip, Color(50, 140, 0))
        #Fill down with random colors
        for i in range(0, LED_COUNT, +5 ):
                for j in range(LED_COUNT+5, i+4, -1):
                        strip.setPixelColor(j-5, Color(0, 0, 0))
                        if j<96:
                                strip.setPixelColor(j+1, Color(50, 140, 0))
                        strip.show()
                        time.sleep(SpeedDelay)
                time.sleep(DisplayDelay)
        time.sleep(PauseDelay)

def FillDownGreenOff(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(50, 140, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +4):
		for j in range(0,LED_COUNT-(i+2)):
			strip.setPixelColor(j, Color(0, 0, 0))
			if j>0:
				strip.setPixelColor(j-4, Color(50, 140, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def BurnOutGreen(strip, red, green, blue, MeteorSize, MeteorTrailDecay, MeteorRandomDecay, SpeedDelay):
	SetAll(strip, Color(50, 140, 0))
	for i in range (0, LED_COUNT + LED_COUNT):
	# Fade brightness all LEDs one step
		for j in range (0, LED_COUNT):
			if ((not MeteorRandomDecay) or ((random.randint(0, 100)>50))):
				FadeToBlack(strip, j, MeteorTrailDecay)
		strip.show()
		time.sleep(SpeedDelay)

def FillDownRed(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(0, 0, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT):
		for j in range(0,LED_COUNT-i):
			strip.setPixelColor(j, Color(128, 2, 0))
			if j>0:
				strip.setPixelColor(j-1, Color(0, 0, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def FillDownRedReverse(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(0, 0, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +8):
		for j in range(LED_COUNT+8, i+7, -1):
			strip.setPixelColor(j-8, Color(128, 2, 0))
			if j<96:
				strip.setPixelColor(j+1, Color(0, 0, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def FillDownRedReverseOff(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
        SetAll(strip, Color(128, 2, 0))
        #Fill down with random colors
        for i in range(0, LED_COUNT, +5 ):
                for j in range(LED_COUNT+5, i+4, -1):
                        strip.setPixelColor(j-5, Color(0, 0, 0))
                        if j<96:
                                strip.setPixelColor(j+1, Color(128, 2, 0))
                        strip.show()
                        time.sleep(SpeedDelay)
                time.sleep(DisplayDelay)
        time.sleep(PauseDelay)

def FillDownRedOff(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(128, 2, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +4):
		for j in range(0,LED_COUNT-(i+2)):
			strip.setPixelColor(j, Color(0, 0, 0))
			if j>0:
				strip.setPixelColor(j-4, Color(128, 2, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def BurnOutRed(strip, red, green, blue, MeteorSize, MeteorTrailDecay, MeteorRandomDecay, SpeedDelay):
	SetAll(strip, Color(128, 2, 0))
	for i in range (0, LED_COUNT + LED_COUNT):
	# Fade brightness all LEDs one step
		for j in range (0, LED_COUNT):
			if ((not MeteorRandomDecay) or ((random.randint(0, 100)>50))):
				FadeToBlack(strip, j, MeteorTrailDecay)
		strip.show()
		time.sleep(SpeedDelay)

def FillDownPurple(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(0, 0, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +5):
		for j in range(0,LED_COUNT-i):
			strip.setPixelColor(j, Color(200, 4, 100))
			if j>0:
				strip.setPixelColor(j-5, Color(0, 0, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def FillDownPurpleReverse(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(0, 0, 0))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +8):
		for j in range(LED_COUNT+8, i+7, -1):
			strip.setPixelColor(j-8, Color(200, 4, 100))
			if j<96:
				strip.setPixelColor(j+1, Color(0, 0, 0))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def FillDownPurpleReverseOff(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
        SetAll(strip, Color(200, 4, 100))
        #Fill down with random colors
        for i in range(0, LED_COUNT, +5 ):
                for j in range(LED_COUNT+5, i+4, -1):
                        strip.setPixelColor(j-5, Color(0, 0, 0))
                        if j<96:
                                strip.setPixelColor(j+1, Color(200, 4, 100))
                        strip.show()
                        time.sleep(SpeedDelay)
                time.sleep(DisplayDelay)
        time.sleep(PauseDelay)

def FillDownPurpleOff(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
	SetAll(strip, Color(200, 4, 100))
	#Fill down with random colors
	for i in range(0, LED_COUNT, +4):
		for j in range(0,LED_COUNT-(i+2)):
			strip.setPixelColor(j, Color(0, 0, 0))
			if j>0:
				strip.setPixelColor(j-4, Color(200, 4, 100))
			strip.show()
			time.sleep(SpeedDelay)
		time.sleep(DisplayDelay)
	time.sleep(PauseDelay)

def BurnOutPurple(strip, red, green, blue, MeteorSize, MeteorTrailDecay, MeteorRandomDecay, SpeedDelay):
	SetAll(strip, Color(200, 4, 100))
	for i in range (0, LED_COUNT + LED_COUNT):
	# Fade brightness all LEDs one step
		for j in range (0, LED_COUNT):
			if ((not MeteorRandomDecay) or ((random.randint(0, 100)>50))):
				FadeToBlack(strip, j, MeteorTrailDecay)
		strip.show()
		time.sleep(SpeedDelay)

def HalloweenRandomColors(strip, SpeedDelay):
    SetAll(strip, Color(0, 0, 0))
    while True:
        for i in range(0, LED_COUNT):
            r=random.randint(0, 45)
            g=random.randint(0, 85)
            b=random.randint(0, 85)
            strip.setPixelColor(i, Color(r, g, b))
        strip.show()
        time.sleep(SpeedDelay)


def FillDownTestReverse(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
        SetAll(strip, Color(0, 0, 0))
        #Fill down with random colors
        for i in range(0, LED_COUNT, +5):
                for j in range(LED_COUNT+5, i+4, -1):
                        strip.setPixelColor(j-5, Color(0, 0, 255))
                        if j<96:
                                strip.setPixelColor(j, Color(0, 0, 0))
                        strip.show()
                        time.sleep(SpeedDelay)
                time.sleep(DisplayDelay)
        time.sleep(PauseDelay)

def FillDownTest(strip, SpeedDelay, DisplayDelay, PauseDelay, FlushDelay):
        SetAll(strip, Color(0, 0, 0))
        #Fill down with random colors
        for i in range(0, LED_COUNT, +5):
                for j in range(0,LED_COUNT-i):
                        strip.setPixelColor(j, Color(128, 2, 0))
                        if j>0:
                                strip.setPixelColor(j-5, Color(0, 0, 0))
                        strip.show()
                        time.sleep(SpeedDelay)
                time.sleep(DisplayDelay)
        time.sleep(PauseDelay)
