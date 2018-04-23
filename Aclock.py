import time
import board
import neopixel

colour = 0x3333ff
tf = '{:02}:{:02}:{:02}'
hours = minutes = seconds = 0

fontb = {'0': [9, 6, 2, 6, 9],
         '1': [0, 8, 8, 16],
         '2': [0, 1, 1, 3, 4, 2, 1, 3, 2, 2, 1, 3, 2, 4, 2, 1],
         '3': [0, 1, 1, 4, 1, 1, 1, 3, 1, 2, 2, 2, 1, 3, 1, 1, 3, 1, 2, 1],
         '4': [4, 8, 1, 6, 1, 4, 8],
         '5': [4, 2, 1, 1, 1, 3, 1, 2, 2, 2, 1, 3, 1, 1, 3, 3, 1],
         '6': [0, 1, 3, 1, 2, 1, 1, 2, 1, 3, 2, 3, 1, 2, 1, 1, 2, 3, 1, 1],
         '7': [1, 4, 3, 3, 1, 3, 2, 2, 1, 9, 3],
         '8': [0, 1, 3, 1, 2, 1, 1, 2, 1, 3, 2, 2, 1, 3, 1, 1, 2, 1, 3, 1],
         '9': [0, 1, 2, 9, 1, 2, 2, 2, 1, 4, 7, 1],
         ':': [0, 2, 1, 2, 1, 10]}
font = {}
for k, v in fontb.items():
    font[k] = []
    f = True
    for i in v:
        font[k] = font[k] + i * [f]
        f = not f
del (fontb)
print(len(font))


def drawtime(t, p, c):
    p.fill((0, 0, 0,))
    fb = [j for i in t for j in font[i]]
    fb = fb + 4 * 8 * [False]
    for i in fb:
        p[i] = fb[i] * c
    p.show()


pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
pixels.fill((0, 0, 0,))
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
