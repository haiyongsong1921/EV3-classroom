from ev3dev2.motor import MoveSteering
from ev3dev2.sensor.lego import GyroSensor
import time
import sys
import math

class GyroCar:
    def __init__(self, left_motor_port, right_motor_port, gyro_mode):
        self.__moveSteering = MoveSteering(left_motor_port, right_motor_port)
        self.__gyro = GyroSensor()
        self.__gyro.mode = gyro_mode

    def __run_forward(self):
        self.__moveSteering.on(0, 20)

    def run_rotations(self, rotations):
        self.__moveSteering.on_for_rotations(0, 20, rotations)

    def stop(self):
        self.__moveSteering.off()

    def __back_and_turn(self, steering):
        self.__moveSteering.on_for_rotations(-steering, 20, -1)

    def reset_angle(self):
        self.__gyro.reset()

    def is_on_flat(self):
        print("is_on_flat: %d" % self.__gyro.angle)
        time.sleep(1)
        return (math.fabs(self.__gyro.angle) < 10)

    def is_on_slope(self):
        print("is_on_slope: %d" % self.__gyro.angle)
        time.sleep(1)
        return (math.fabs(self.__gyro.angle) >= 10)

    def run(self):
        self.__run_forward()

    @property
    def angle(self):
        return self.__gyro.angle
        
        