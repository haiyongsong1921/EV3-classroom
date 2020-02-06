from ev3dev2.motor import MoveSteering
from ev3dev2.sensor.lego import InfraredSensor, TouchSensor
from ev3dev2.sound import Sound

class AutoCar:
    def __init__(self, left_motor_port, right_motor_port):
        self.__movesteering = MoveSteering(left_motor_port, right_motor_port)
        self.__touch = TouchSensor()

    def __run_forward(self):
        self.__movesteering.on(0, 30)

    def __stop(self):
        self.__movesteering.off()

    def __play_text_sound(self, words):
        sound = Sound()
        sound.speak(words)

    def __back_left(self):
        self.__movesteering.on_for_rotations(50, 20, -1)

    def __touch_sensor_pressed(self):
            return self.__touch.is_pressed
            
    def __touch_execute(self):
        self.__stop()
        self.__play_text_sound("Ouch") #take some time, consume resource
        self.__back_left()

    def run(self):
        self.__run_forward()
        touched = self.__touch_sensor_pressed()
        if(touched):
            self.__touch_execute()

        
