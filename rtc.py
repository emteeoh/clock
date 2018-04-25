import board
import busio
import adafruit_ds3231
import time


def foo():
    i2c = busio.I2C(board.SCL, board.SDA)
    ds3231 = adafruit_ds3231.DS3231(i2c)
    while True:
        print("{3:02}:{4:02}:{5:02}".format(*ds3231.datetime))
        time.sleep(1)
