#!/usr/bin/env pybricks-micropython

# from pybricks import ev3brick as brick
# from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
#                                  InfraredSensor, UltrasonicSensor, GyroSensor)
# from pybricks.parameters import (Port, Stop, Direction, Button, Color,
#                                  SoundFile, ImageFile, Align)
# from pybricks.tools import print, wait, StopWatch
# from pybricks.robotics import DriveBase

from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveTank
from ev3dev2.sensor.lego import UltrasonicSensor, InfraredSensor
from ev3dev2.sensor import INPUT_1
import time

# def top_left_channel_1_action(state):
#     print("top left on channel 1: %s" % state)

# def bottom_right_channel_4_action(state):
#     print("bottom right on channel 4: %s" % state)

# ir = InfraredSensor()
# ir.on_channel1_top_left = top_left_channel_1_action
# ir.on_channel4_bottom_right = bottom_right_channel_4_action

# while True:
#     ir.process()
#     time.sleep(0.01)


tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)
#tank_drive.cs = ColorSensor()
ultra_sensor = UltrasonicSensor()

def drive_backword_by_round(wheel_round):
    tank_drive.on_for_rotations(-30, -30, wheel_round)

def drive_turn_left():
    tank_drive.on_for_rotations(0, 20, 1)

while True:
    tank_drive.on(30, 30)
    distance = ultra_sensor.distance_centimeters
    if (distance < 30):
        drive_backword_by_round(1)
        drive_turn_left()
        time.sleep(0.2)
