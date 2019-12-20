#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from math import sin
# Write your program here

watch = StopWatch()
amplitude = 90

brick.sound.beep()
motor_l = Motor(Port.A)
motor_r = Motor(Port.D)



#while True:
    # seconds = watch.time()/1000
    # print(seconds)
    # angle_now = sin(seconds)*amplitude
    # motor_l.track_target(angle_now)
    