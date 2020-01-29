#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from ev3dev2.motor import OUTPUT_A, OUTPUT_D#, MoveTank, MoveSteering
from ev3dev2.sensor.lego import UltrasonicSensor, InfraredSensor
from ev3dev2.sensor import INPUT_1
from TankDrive import TankDrive
import time

# Write your program here
brick.sound.beep()

tank_drive = TankDrive(OUTPUT_A, OUTPUT_D)#MoveTank(OUTPUT_A, OUTPUT_D)
#steering_drive = MoveSteering(OUTPUT_A, OUTPUT_D)

#tank_drive.cs = ColorSensor()
ultra_sensor = UltrasonicSensor()

while True:
    tank_drive.on(30, 30)
    distance = ultra_sensor.distance_centimeters
    if (distance < 30):
        tank_drive.drive_turn_left()
        time.sleep(0.2)