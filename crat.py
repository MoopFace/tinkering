#!/user/bin/python3.7

import gpiozero
import time

pin1 = led(2)
pin2 = led(3)
pin3 = led(4)
pin4 = led(17)

pin1.on
sleep(1)
pin1.off
pin2.on
sleep(1)
pin2.off
pin3.on
sleep(1)
pin3.off
pin4.on
sleep(1)
pin4.off
