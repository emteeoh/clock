import board
import neopixel
import gc


def foo():
    print('0', gc.mem_free())
    tf = '{:02}{:02}{:02}'
    hours = minutes = seconds = 0
    print("1", gc.mem_free())

    fontb = {'0': [9, 6, 2, 6, 9]
        , '1': [0, 8, 8, 16]
        , '2': [0, 1, 1, 3, 4, 2, 1, 3, 2, 2, 1, 3, 2, 4, 2, 1]
        , '3': [0, 1, 1, 4, 1, 1, 1, 3, 1, 2, 2, 2, 1, 3, 1, 1, 3, 1, 2, 1]
        , '4': [4, 8, 1, 6, 1, 4, 8]
        , '5': [4, 2, 1, 1, 1, 3, 1, 2, 2, 2, 1, 3, 1, 1, 3, 3, 1]
        , '6': [0, 1, 3, 1, 2, 1, 1, 2, 1, 3, 2, 3, 1, 2, 1, 1, 2, 3, 1, 1]
        , '7': [1, 4, 3, 3, 1, 3, 2, 2, 1, 9, 3]
        , '8': [0, 1, 3, 1, 2, 1, 1, 2, 1, 3, 2, 3, 1, 2, 1, 1, 2, 1, 3, 1]
        , '9': [0, 1, 2, 9, 1, 2, 2, 2, 1, 4, 7, 1]
        , ':': [0, 2, 1, 2, 1, 10]
             }
    print("2", gc.mem_free())

    pixels = neopixel.NeoPixel(board.D4, 256, brightness=0.3, bpp=3, auto_write=False)
    pixels.fill((0, 0, 0))
    pixels.show()
    print("3", gc.mem_free())

    font = {}
    for k, v in fontb.items():
        font[k] = []
        f = True
        for i in v:
            font[k] = font[k] + i * [f]
            f = not f
    print("4", gc.mem_free())

    del fontb
    print("5", gc.mem_free())

    for i, j in enumerate(font['0']):
        pixels[i] = j * 0x3333ff
    print("6", gc.mem_free())
    pixels.show()
