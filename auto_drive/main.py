#!/usr/bin/env python3
from AutoDrive import AutoDrive
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_D


sound = Sound()
sound.beep()

autoDrive = AutoDrive(OUTPUT_A, OUTPUT_D, 'IR-PROX', 'US-DIST-CM')

while True:
    autoDrive.run()