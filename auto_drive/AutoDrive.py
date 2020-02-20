from ev3dev2.motor import MediumMotor, MoveSteering
from ev3dev2.sensor.lego import InfraredSensor, UltrasonicSensor
import time
import sys

class AutoDrive:
    def __init__(self, left_motor_port, right_motor_port, infra_mode, ultra_mode):
        self.__moveSteering = MoveSteering(left_motor_port, right_motor_port)
        self.__mediumMotor = MediumMotor()
        self.__ir = InfraredSensor()
        self.__ir.mode = infra_mode
        self.__us = UltrasonicSensor()
        self.__us.mode = ultra_mode

    def __run_forward(self):
        self.__moveSteering.on(0, 30)

    def __run_backward_rotations(self, rotations):
        self.__moveSteering.on_for_rotations(0, 20, -rotations)

    def __stop(self):
        self.__moveSteering.off()

    def __back_and_turn(self, steering):
        self.__moveSteering.on_for_rotations(-steering, 20, -1)

    def __scan_around_distance(self):
        proximities = {}
        distance = 0
        index = 0
        for deg in [-90, 30, 30, 30, 30, 30, 30]:
            self.__mediumMotor.on_for_degrees(10, deg)
            distance = self.__ir.proximity
            proximities[-90+index*30] = distance
            index += 1
            time.sleep(1)
        self.__mediumMotor.on_for_degrees(10, -90)
       # print("%s" % proximities)
        return proximities

    def __find_clear_direction(self, proximitiesDic):
        max_distance = max(list(proximitiesDic.values()))
        direction = list(proximitiesDic.keys())[list(proximitiesDic.values()).index(max_distance)]
        #print("%d" % direction)
        steering = self.__convert_direction_to_steering(direction)
        return steering

    def __convert_direction_to_steering(self, direction):
        return 5*direction/9

    def __ultrasonic_distance(self):
        return self.__us.distance_centimeters

    def run(self):
        self.__run_forward()
        block_distance = self.__ultrasonic_distance()
        if(block_distance < 20):
            self.__stop()
            around_distance = self.__scan_around_distance()
            steering = self.__find_clear_direction(around_distance)
            self.__run_backward_rotations(0.5)
            self.__back_and_turn(steering)
