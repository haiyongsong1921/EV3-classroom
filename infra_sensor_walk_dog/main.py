#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick

from WalkDog import WalkDog
from ev3dev2.motor import OUTPUT_A, OUTPUT_D
import time
import sys


brick.sound.beep()

steering_drive = WalkDog(OUTPUT_A, OUTPUT_D, 'IR-SEEK')
#steering_drive.ir.mode = 'IR-SEEK'

while True:
    steering_drive.run(1)

