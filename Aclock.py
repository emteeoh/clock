import time
import board
import neopixel
from fontdef import *


def foo():
    colour = 0x3333ff
    tf = '{:02}:{:02}:{:02}'
    hours = minutes = seconds = 0

    def drawtime(t, p, c):
        p.fill((0, 0, 0,))
        offset = 0
        for digit in t:
            for i, j in enumerate(font[fontmap.index(digit)]):
                p[i + offset] = j * c
            offset += len(font[fontmap.index(digit)])
        p.show()

    pixels = neopixel.NeoPixel(board.D4, 256, bpp=3, brightness=0.3, auto_write=False)
    pixels.fill((0, 0, 0))
    pixels.show()
    while True:
        currenttime = tf.format(hours, minutes, seconds)
        drawtime(currenttime, pixels, colour)
        time.sleep(1)
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
                if hours == 24:
                    hours = 0
