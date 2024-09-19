import RPi.GPIO as gp
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0, 0, 0, 0, 0, 0, 0, 0]
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)

for i in range(8):
    gp.output(dac[i], number[i])
time.sleep(15)
gp.output(dac, 0)
gp.cleanup()

