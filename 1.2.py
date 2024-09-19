import RPi.GPIO as gp
import time

leds = [2, 3, 4, 17, 27, 22, 10, 9]
gp.setmode(gp.BCM)
gp.setup(leds, gp.OUT)

for k in range(3):
    for i in range(9):
        gp.output(leds[i%8], 1)
        time.sleep(0.2)
        gp.output(leds[i%8], 0)

gp.output(leds, 0)
gp.cleanup()