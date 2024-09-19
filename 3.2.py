import RPi.GPIO as gp
import time

leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]
gp.setmode(gp.BCM)
gp.setup(leds, gp.OUT)
gp.setup(aux, gp.IN)

while True:
    for i in range(8):
        gp.output(leds[i], gp.input(aux[i]))
        time.sleep(0.2)
