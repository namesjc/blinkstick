#!/usr/bin/env python

import time
from blinkstick import blinkstick
from random import randint
import os

dir = "/home/pi/pixels/"


class Main(blinkstick.BlinkStickPro):
    def run(self):
        self.send_data_all()

        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)

        while True:
            no_pixels = 8

            for i in range(0, 8):
                if os.path.isfile(dir + str(i)):
                    # print(i)
                    time.sleep(0.003)
                    self.bstick.set_color(0, i, 0, 10, 0)
                    no_pixels += 1
                else:
                    time.sleep(0.003)
                    self.bstick.set_color(0, i, 0, 0, 0)
                    # print(i)
                    no_pixels -= 1

            # self.bstick.device.reset()
            time.sleep(0.2)

            if no_pixels == 0:
                for i in range(0, 8):
                    self.clear()
                    time.sleep(0.003)
                    self.bstick.set_color(0, i, 0, 0, 0)
                # self.bstick.device.reset()


# Change the number of LEDs for r_led_count
main = Main(r_led_count=8, max_rgb_value=128)
if main.connect():
    main.run()
else:
    print("No BlinkSticks found")


