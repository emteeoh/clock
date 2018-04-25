import time
import board
import neopixel
from fontdef import *
import busio
import adafruit_ds3231
import gc


def foo():
    tf = '{3:02}:{4:02}:{5:02}'
    ds3231 = adafruit_ds3231.DS3231(busio.I2C(board.SCL, board.SDA))
    while True:
        print(gc.mem_free())
        with neopixel.NeoPixel(board.D1, 224, bpp=3, brightness=0.1, auto_write=False) as p:
            print(gc.mem_free())
            p.fill((0, 0, 0,))
            offset = 0
            for digit in tf.format(*ds3231.datetime):
                for i, j in enumerate(font[fontmap.index(digit)]):
                    p[i + offset] = j * 0x3333ff
                offset += len(font[fontmap.index(digit)])
            print(gc.mem_free())
            p.show()
            print(gc.mem_free())
        time.sleep(1)


'''
gc outputs with 2.2.4:
1312
528
5248




'''
