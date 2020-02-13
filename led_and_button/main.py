#!/usr/bin/env python3

from ev3dev2.button import Button
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

sound = Sound()
sound.beep()

button = Button()
leds = Leds()

while True:
    if(button.right):
        leds.animate_cycle(('RED', 'GREEN', 'AMBER', 'ORANGE', 'YELLOW'))
    elif(button.left):
        leds.animate_flash('RED', sleeptime=0.5, duration=5)
    elif(button.down):
        leds.animate_police_lights('RED', 'GREEN', sleeptime=0.5, duration=5)
    elif(button.up):
        leds.animate_rainbow(increment_by=0.1, sleeptime=0.1, duration=10)
    else:
        leds.all_off()
# Write your program here


