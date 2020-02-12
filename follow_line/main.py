#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound
from ColorTank import ColorTank
import time
import sys

sound = Sound()
# tank = MoveTank(OUTPUT_A, OUTPUT_D)
# tank.cs = ColorSensor()

color_tank = ColorTank(OUTPUT_A, OUTPUT_D, 'IR-REMOTE', 'COL-COLOR')
sound.beep()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

while True:    
    color_tank.process()
    time.sleep(2)
  

# try:
#     Follow the line for 4500ms
#     tank.follow_line(
#         kp=11.3, ki=0.05, kd=3.2,
#         speed=SpeedPercent(30),
#         follow_for=follow_for_ms,
#         ms=4500
#     )

# except Exception:
#     tank.stop()
#     raise

