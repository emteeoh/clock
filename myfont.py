import board
import neopixel
import gc
import time
from fontdef import *

ff = [9]

def foo():
    print('0', gc.mem_free())
    tf = '{:02}{:02}{:02}'
    hours = minutes = seconds = 0
    print("1", gc.mem_free())
    print("2", gc.mem_free())
    pixels = neopixel.NeoPixel(board.D4, 256, brightness=0.3, bpp=3, auto_write=False)
    pixels.fill((0, 0, 0))
    pixels.show()
    print("3", gc.mem_free())
    print("4", gc.mem_free())
    for o, c in enumerate(fontmap):
        for i, j in enumerate(font[o]):
            pixels[i] = j * 0x3333ff
        print("5", gc.mem_free())
        pixels.show()
        time.sleep(0.25)
    print("6", gc.mem_free())
