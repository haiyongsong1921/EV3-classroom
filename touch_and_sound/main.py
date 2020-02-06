#!/usr/bin/env python3

#from pybricks import ev3brick as brick

from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_D
from AutoCar import AutoCar

# Write your program here
#brick.sound.beep()

auto_car = AutoCar(OUTPUT_A, OUTPUT_D)
sound = Sound()
sound.beep()

while True:
    auto_car.run()

