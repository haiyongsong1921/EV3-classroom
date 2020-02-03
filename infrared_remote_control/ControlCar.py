from ev3dev2.motor import MoveSteering, SpeedPercent, 
from ev3dev2.sensor.lego import InfraredSensor
import sys
import math

class ControlCar:
    def __init__(self, left_motor_port, right_motor_port, sensor_mode):
        self.__movesteering = MoveSteering(left_motor_port, right_motor_port)
        self.__ir = InfraredSensor()
        self.__ir.mode = sensor_mode
        # self.__ir.on_channel1_top_left = self.__top_left_channel_1_action
        # self.__ir.on_channel1_top_right = self.__top_right_channel_1_action


    def __turn_left(self):
        self.__movesteering.on(-50, 30)

    def __turn_right(self):
        self.__movesteering.on(50, 30)
        # if(state):
        #     self.__movesteering.on(50, 30)
        # else:
        #     self.__movesteering.off()
    def __run_forward(self):
        self.__movesteering.on(0, 30)

    def __run_backward(self):
        self.__movesteering.on(0, -20)

    def __stop(self):
        self.__movesteering.off()

    def __get_button_pressed_value(self, buttons):
        BUTTON_VALUES = {
            0: [],
            1: ['top_left'],
            2: ['bottom_left'],
            3: ['top_right'],
            4: ['bottom_right'],
            5: ['top_left', 'top_right'],
            6: ['top_left', 'bottom_right'],
            7: ['bottom_left', 'top_right'],
            8: ['bottom_left', 'bottom_right'],
            9: ['beacon'],
            10: ['top_left', 'bottom_left'],
            11: ['top_right', 'bottom_right']
            }
        return list(BUTTON_VALUES.keys())[list(BUTTON_VALUES.values()).index(buttons)]

    def __run(self, button_value):
        if(button_value == 1):
            self.__turn_left()
        elif(button_value == 3):
            self.__turn_right()
        elif(button_value == 5):
            self.__run_forward()
        elif(button_value == 8):
            self.__run_backward()
        else:
            self.__stop()

    def process(self):
        self.__ir.process()
        buttons_pressed = self.__ir.buttons_pressed()
        button_value = self.__get_button_pressed_value(buttons_pressed)
        self.__run(button_value)
        
