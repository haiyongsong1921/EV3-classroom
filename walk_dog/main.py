#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()

motor_l = Motor(Port.A)
motor_r = Motor(Port.D)

#init a infrared sensor
infrared = InfraredSensor(Port.S3)

robot = DriveBase(motor_l, motor_r, 56, 114)
sensor = UltrasonicSensor(Port.S1)

robot.drive(300,0)
while sensor.distance() > 200:
    wait(10)
robot.stop()
# while True:
#     # distance_current = infrared.distance()
#     # print(distance_current)
#     beacon_position_tuple = infrared.beacon(1)
#     print(beacon_position_tuple)
#    # wait(1000)

#     brick.display.clear()
#     brick.display.text(beacon_position_tuple[0], (30, 20))
#     brick.display.text(beacon_position_tuple[1], (30, 40))

