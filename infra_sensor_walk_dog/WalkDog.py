from ev3dev2.motor import MoveTank, MoveSteering, SpeedPercent, LargeMotor
from ev3dev2.sensor.lego import InfraredSensor
import sys
import math

class WalkDog:
    def __init__(self, left_motor_port, right_motor_port, sensor_mode):
        self._movesteering = MoveSteering(left_motor_port, right_motor_port)
        self._ir = InfraredSensor()
        self._ir.mode = sensor_mode

    @property
    def ir(self):
        return self._ir

    @ir.setter
    def ir(self, ir):
        self._ir = ir

    @property
    def movesteering(self):
        return _movesteering

    @movesteering.setter
    def movesteering(self, ms):
        self._movesteering = ms

    def convert_heading_to_steering(self, heading):
        return heading*2

    def run(self, channel=1):
        beacon_distance = self._ir.distance(channel)
        head_angle = self._ir.heading(channel)
        steering = self.convert_heading_to_steering(head_angle)
        if(beacon_distance > 30 ):
            self._movesteering.on(steering, 50)
        else:
            self._movesteering.off()

# class SteeringDrive(MoveSteering):
#     def __init__(self, left_motor_port, right_motor_port, desc=None, motor_class=LargeMotor):
#         super(MoveSteering, self).__init__(left_motor_port, right_motor_port)
#         self._ir = InfraredSensor()

#     @property
#     def ir(self):
#         return self._ir

#     @ir.setter
#     def ir(self, ir):
#         self._ir = ir

#     def convert_heading_to_steering(self, heading):
#         return heading*2

#     # def drive_toward_beacon(self, channel=1):
#     #     head_angle = self._ir.heading(channel)
#     #     steering = self.convert_heading_to_steering(head_angle)
#     #     #print("%s" % steering)
#     #     # if(abs(steering) > 20):
#     #     #     MoveSteering.on_for_rotations(self, steering, SpeedPercent(50), 1.4)
#     #     return steering

#     def drive_walk_dog(self, channel=1):
#         beacon_distance = self._ir.distance(channel)
#         head_angle = self._ir.heading(channel)
#         steering = self.convert_heading_to_steering(head_angle)
#         if(beacon_distance > 30 ):
#             MoveSteering.on(self, steering, 50)
#         else:
#             MoveSteering.off(self)
