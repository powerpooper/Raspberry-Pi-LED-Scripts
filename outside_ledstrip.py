#!/usr/bin/python
# -*- coding: utf-8 -*-

###		OUTSIDE		###

#Import the 'functions_library' which animates the LEDs in various ways.
from holidaylib import *
from varfile import *
import psutil

LED_STRIP = ws.WS2811_STRIP_RGB   # Strip type and colour ordering



try:
    file_name =  os.path.basename(sys.argv[0])
    colornow = sys.argv[1].lstrip('#')
except:
    print

pid = str(os.getpid())
def updateAnimationPid():
	with open("/usr/lib/cgi-bin/varfile.py") as f:
		for line in f:
			if "Animation =" in line:
				curval=line
				s = open("/usr/lib/cgi-bin/varfile.py").read()
				s = s.replace('%s' % curval, "Animation = " + pid + "\n")
				f = open("/usr/lib/cgi-bin/varfile.py", 'w')
				f.write(s)
				f.close()

def updateAnimationOff():
	with open("/usr/lib/cgi-bin/varfile.py") as f:
		for line in f:
			if "Animation =" in line:
				curval=line
				s = open("/usr/lib/cgi-bin/varfile.py").read()
				s = s.replace('%s' % curval, "Animation = False\n")
				f = open("/usr/lib/cgi-bin/varfile.py", 'w')
				f.write(s)
				f.close()

# If the colornow is a HEX value, convert it to RGB
def hexColorRGB(colornow):
        hlen = len(colornow)
        return tuple(int(colornow[i:i+hlen/3], 16) for i in range(0, hlen, hlen/3))

# If the colornow is a HEX value, convert it to RGB
def hexLastRGB(lastcolor):
        lastcolorhex = lastcolor.lstrip('#')
        hlen = len(lastcolorhex)
        return tuple(int(lastcolorhex[i:i+hlen/3], 16) for i in range(0, hlen, hlen/3))

# If the colornow is a HEX value, convert it to RGB
def hexWhiteRGB(whiteRGB):
        whitehex = whiteRGB.lstrip('#')
        hlen = len(whitehex)
        return tuple(int(whitehex[i:i+hlen/3], 16) for i in range(0, hlen, hlen/3))=

whiteRGB = '#FF9329'
getWhite = hexWhiteRGB(whiteRGB)
whitecolor = Color(getWhite[0], getWhite[1], getWhite[2])

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Define functions which animate LEDs in various ways.
def colorWipeEnd(strip, color, wait_ms=5):
	"""Wipe color across display a pixel at a time."""
    	for i in range(strip.numPixels()):
        	strip.setPixelColor(i, color)
        	strip.show()
		time.sleep(wait_ms/1000.0)

def wheelNewColor(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos > 96:
        return newcolor
    elif pos > 96:
        pos += 0
        return red
    else:	
        pos -= 0
        return bakcolor
		
def colorWipeNewColor(strip, wait_ms=10, iterations=110):
    """Wipe color across display a pixel at a time."""	
    for j in range(iterations):				
        for i in range(strip.numPixels()):		
            strip.setPixelColor(i, wheelNewColor((i+j)));
        strip.show()
        time.sleep(wait_ms/1000.0)			
		
def colorChange():
	colorWipeNewColor(strip)


#################### 						####################
#################### 		Rainbow Funvtions		####################
#################### 		     Start			####################
#################### 						####################

# Define functions which animate LEDs in various ways.
def colorWipeRainbowEnd(strip, color, wait_ms=5):
	"""Wipe color across display a pixel at a time."""
    	for i in range(strip.numPixels()):
        	strip.setPixelColor(i, color)
        	strip.show()
		time.sleep(wait_ms/1000.0)

def wheelRainbow(pos):
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
            strip.setPixelColor(i, wheelRainbow((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)




#################### 						####################
#################### 		Christmas Funvtions		####################
#################### 		       Start			####################
#################### 						####################

# Define functions which animate LEDs in various ways.
def christmasWipe(strip, color, wait_ms=5):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

# Define functions which animate LEDs in various ways.
def christmasWipeNew(strip, color, wait_ms=5):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
	strip.show()
	time.sleep(wait_ms/1000.0)

# Define functions which animate LEDs in various ways.
def christmasWipeEnd(strip, color, wait_ms=5):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def wheelNewChristmas(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos > 206:
		return whitecolor
	elif pos > 206:
		pos += 0
		return red
	else:
		pos -= 0
		return bakcolor

def christmasWipeNewColor(strip, wait_ms=5,  iterations=208):
	"""Wipe color across display a pixel at a time."""
	for j in range(iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheelNewChristmas((i+j)));
		strip.show()
		time.sleep(wait_ms/1000.0)

def colorChristmas():
	christmasWipeNewColor(strip)

def christmasColor():
	# Blue
	colorChristmas()
	FillDownBlue(strip, .001, .001, .001, .1)
	ChristmasChaseBlue(strip, 255, 147, 41, .1, 2000)

	# Sparkle
	christmasWipe(strip, 0, 0, 80, .015)
	t_end = time.time() + 60 * 3
	while time.time() < t_end:
		SnowSparkle(strip, 0, 0, 80, .1, random.uniform(0, .5))
	time.sleep(1)

	# Red
	EveryOtherRed(strip, .03, .03, .03, .1)
	ChristmasChaseRed(strip, 255, 0, 0, .16, 2000)

	gc.collect()


#################### 						####################
#################### 		Halloween Funvtions		####################
#################### 		       Start			####################
#################### 						####################

def colorWheelHalloween(pos):
	"""Generate rainbow colors across 0-255 positions."""
    	if pos > 206:
		return newcolor
    	elif pos > 206:
        	pos += 0
        	return red
    	else:
        	pos -= 0
        	return bakcolor

def colorWipeNewHalloween(strip, wait_ms=5, iterations=208):
	"""Wipe color across display a pixel at a time."""
	for j in range(iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, colorWheelHalloween((i+j)));
        	strip.show()
        	time.sleep(wait_ms/1000.0)

def colorChangeHalloweem():
	colorWipeNewHalloween(strip)

def halloweenColor():
	# Orange
	RunningLightsSnakeReverse(strip, 255, 60, 0, 7)
	colorWipeHalloweenEnd(strip, Color(255,60,0), 5)
	colorWipeHalloweenEnd(strip, Color(0,0,0), 5)
	NewKitt(strip, 255, 60, 0, 32, .01, .05)
	FillDownOrangeReverse(strip, .01, .01, 45, .05)
	colorWipeHalloweenEnd(strip, Color(0,0,0), 15)

	# Green
	RunningLightsSnakeReverse(strip, 50, 140, 0, 7)
	colorWipeHalloweenEnd(strip, Color(50,140,0), 5)
	colorWipeHalloweenEnd(strip, Color(0,0,0), 5)
	NewKitt(strip, 50, 140, 0, 32, .01, .05)
	FillDownGreenReverse(strip, .01, .01, 45, .05)
	colorWipeHalloweenEnd(strip, Color(0,0,0), 5)

	# Red
	RunningLightsSnakeReverse(strip, 255, 4, 0, 7)
	colorWipeHalloweenEnd(strip, Color(255,4,0), 5)
	colorWipeHalloweenEnd(strip, Color(0,0,0), 5)
	NewKitt(strip, 255, 4, 0, 32, .01, .05)
	FillDownRedReverse(strip, .01, .01, 45, .05)
	colorWipeHalloweenEnd(strip, Color(0,0,0), 5)

	# Purple
	RunningLightsSnakeReverse(strip, 200, 0, 45, 7)
	colorWipeHalloweenEnd(strip, Color(200,0,45), 5)
	colorWipeHalloweenEnd(strip, Color(0,0,0), 5)
	NewKitt(strip, 200, 0, 45, 32, .01, .05)
	FillDownPurpleReverse(strip, .01, .01, 45, .05)
	colorWipeHalloweenEnd(strip, Color(0,0,0), 5)

	gc.collect()

def quit_Animation(*args):
	result=Animation
	lastcolornum = hexLastRGB(lastcolor)
	colorWipeEnd(strip, Color(lastcolornum[0], lastcolornum[1], lastcolornum[2]), 5)
#	colorWipeEnd(strip, Color(0,0,0), 5)
	time.sleep(2)
	updateAnimationOff()
	sys.exit(0)


if Power == "on":
	#Main program logic:
	if __name__ == '__main__':

		#Process arguments
		signal.signal(signal.SIGINT, quit_Animation)

	        #Create NeoPixel object with appropriate configuration.
	        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	        #Intialize the library (must be called once before other functions).
	        strip.begin()

		while True:
		        animationpid = psutil.pid_exists(Animation)

		        if animationpid in [False]:
		                break

		        time.sleep(0.1)


### Rainbow ###
		if colornow == "rainbow":

			lastcolornum = hexLastRGB(lastcolor)
			bakcolor = Color(lastcolornum[0], lastcolornum[1], lastcolornum[2])

			# Updating Animation PID
			updateAnimationPid()

			try:
				while 1:
					rainbowCycle(strip)
				pass

			except KeyboardInterrupt:
				if quit_Animation():
					print("Done")

### Christmas ###
		elif colornow == "christmas":

			# Updating Animation PID
			updateAnimationPid()

			try:

		                while 1:
					christmasColor()
	                        pass

			except KeyboardInterrupt:
				if quit_Animation():
					print("Done")

### Halloween ###
		elif colornow == "halloween":

			# Updating Animation PID
			updateAnimationPid()

			try:
				while 1:
					halloweenColor()
				pass

			except KeyboardInterrupt:
				if quit_Animation():
					print("Done")

		### Main Colors ###
		else:

			def updateLastColor():
				with open("/usr/lib/cgi-bin/varfile.py") as f:
					for line in f:
						if "lastcolor =" in line:
							curval=line
							s = open("/usr/lib/cgi-bin/varfile.py").read()
							s = s.replace('%s' % curval, "lastcolor = "'"#' + colornow + '"'"\n")
							f = open("/usr/lib/cgi-bin/varfile.py", 'w')
							f.write(s)
							f.close()

			# New Color
			colornum = hexColorRGB(colornow)
			newcolor = Color(colornum[0], colornum[1], colornum[2])

			# Last Color
			lastcolornum = hexLastRGB(lastcolor)
			bakcolor = Color(lastcolornum[0], lastcolornum[1], lastcolornum[2])
			colorChange()
			updateLastColor()


