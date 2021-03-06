#!/usr/bin/env python
# 0.0.2 - version with pixel controller

import time
import os

dir = "/home/ubuntu/pixels/"

for i in range(9):
    print(i)
    if(i == 8):                                     # If i == 8, the end has been reached and it should not try to enable anymore leds
        print("No more spots left")
        break
    elif not os.path.isfile(dir + str(i)):          # If the file is not there, create it, so the pixel controller will know to turn on the pixel
        print("Pixel ",i," available, activating!")
        f = open(dir + str(i), "a")
        time.sleep(2)
        break

time.sleep(int(os.environ["SLEEP"]))
