#This is the main.  This meeds to import function_library.py in order to work.

#Import the 'functions_library' which animates the LEDs in various ways.
from halloween_library import *
from varfile import *
import argparse
import os


pid = str(os.getpid())
def updateOther():
	with open("varfile.py") as f:
		for line in f:
			if "HALLOWEEN =" in line:
				curval=line
#				print(curval)
				s = open("varfile.py").read()
				s = s.replace('%s' % curval, "HALLOWEEN = " + pid + "\n")
				f = open("varfile.py", 'w')
				f.write(s)
				f.close()

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

def quit_gracefully(*args):
	filename = "/usr/lib/cgi-bin/varfile.py"
	varfile = open(filename, 'r')
	lines=varfile.readlines()
	result=lines[9]
	varfile.close()

	colorWipeEnd(strip, Color(0,0,0), 10)

	sys.exit(0)

# Define functions which animate LEDs in various ways.
def colorWipeEnd(strip, color, wait_ms=20):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
	time.sleep(wait_ms/1000.0)

#Main program logic:
if __name__ == '__main__':
        #Process arguments
	signal.signal(signal.SIGINT, quit_gracefully)
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
	updateOther()

        #Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        #Intialize the library (must be called once before other functions).
        strip.begin()

#        print ('Press Ctrl-C to quit.')
        if not args.clear:
                print('')

        try:

                while 1:
			NewKitt(strip, 255, 60, 0, 8, .01, .05)
			FillDownOrangeReverse(strip, .01, .01, 90, .2)		# Orange
			colorWipeEnd(strip, Color(0,0,0), 15)

			NewKitt(strip, 50, 140, 0, 8, .01, .05)
			FillDownGreenReverse(strip, .01, .01, 90, .2)		# Green
			colorWipeEnd(strip, Color(0,0,0), 15)

			NewKitt(strip, 128, 2, 0, 8, .01, .05)
			FillDownRedReverse(strip, .01, .01, 90, .2)		# Red
			colorWipeEnd(strip, Color(0,0,0), 15)

			NewKitt(strip, 200, 4, 100, 8, .01, .05)
			FillDownPurpleReverse(strip, .01, .01, 90, .2)		# Purple
			colorWipeEnd(strip, Color(0,0,0), 15)

			pass

	except KeyboardInterrupt:
		if quit_gracefully():
			print("Done")
