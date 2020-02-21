#!/usr/bin/env python3
from GyroCar import GyroCar
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_D
import sys


sound = Sound()
sound.beep()

gyroCar = GyroCar(OUTPUT_A, OUTPUT_D, 'GYRO-ANG')
gyroCar.reset_angle()
print("%d" % gyroCar.angle)
reach_slope = False

while True:
    gyroCar.run()
    on_slope = gyroCar.is_on_slope()
    if(on_slope):
        reach_slope = True

    reach_to_top = gyroCar.is_on_flat()
    if(reach_to_top and reach_slope):
        gyroCar.run_rotations(1)
        gyroCar.stop()
        break
