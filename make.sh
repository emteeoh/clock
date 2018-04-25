#!/bin/bash
~/bin/mpy-cross Aclock.py
~/bin/mpy-cross fontdef.py
~/bin/mpy-cross rtc.py
rm -rf /media/richard/CIRCUITPY/lib
mkdir /media/richard/CIRCUITPY/lib
cp lib-2.2.3/neopixel.mpy /media/richard/CIRCUITPY/lib
cp -R lib-2.2.3/adafruit_bus_device /media/richard/CIRCUITPY/lib
cp -R lib-2.2.3/adafruit_register /media/richard/CIRCUITPY/lib
cp *.mpy /media/richard/CIRCUITPY
