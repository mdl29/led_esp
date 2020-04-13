#

#from neopixel import * # vrai neopixel

import time
from vrtneopixel import *
import pygame
from pygame.locals import QUIT
import random

# LED strip configuration:
LED_COUNT      = (1, 64)      # Number of LED pixels.
#LED_COUNT      = 10      # Number of LED pixels.
LED_PIN        = 18      # Raspberry Pi GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()


reste = True

while reste:
    for event in pygame.event.get():
        if event.type == QUIT:
            reste = False
    pixel = random.randint(0, 150)
    r_color = random.randint(0, 255)
    b_color = random.randint(0, 255)
    g_color = random.randint(0, 255)
    strip.setPixelColor(pixel, Color(r_color, b_color, g_color)) 
    strip.show()
    time.sleep(50/1000.0)

# sort
