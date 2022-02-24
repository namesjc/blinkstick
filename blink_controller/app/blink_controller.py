#!/usr/bin/env python

import time
from blinkstick import blinkstick
import os

dir = "/home/ubuntu/pixels/"

red = os.getenv("red")
green = os.getenv("green")
blue = os.getenv("blue")

class Main(blinkstick.BlinkStickPro):
    def run(self):
        self.send_data_all()

        while True:
            no_pixels = 8

            for i in range(0, 8):
                if os.path.isfile(dir + str(i)):
                    time.sleep(0.003)
                    self.bstick.set_color(0, i, red, green, blue)
                    no_pixels += 1
                else:
                    time.sleep(0.003)
                    self.bstick.set_color(0, i, blue, green, blue)
                    no_pixels -= 1

            time.sleep(0.2)

            if no_pixels == 0:
                for i in range(0, 8):
                    self.clear()
                    time.sleep(0.003)
                    self.bstick.set_color(0, i, 0, 0, 0)


# Change the number of LEDs for r_led_count
main = Main(r_led_count=8, max_rgb_value=128)
if main.connect():
    main.run()
else:
    print("No BlinkSticks found")


