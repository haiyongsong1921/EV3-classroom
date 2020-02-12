from ev3dev2.motor import MoveSteering, MediumMotor
from ev3dev2.sensor.lego import InfraredSensor, ColorSensor
from ev3dev2.sound import Sound

class ColorTank:
    def __init__(self, left_motor_port, right_motor_port, infra_sensor_mode, color_sensor_mode):
        self.__movesteering = MoveSteering(left_motor_port, right_motor_port)
        self.__mediummotor = MediumMotor()
        self.__cs = ColorSensor()
        self.__cs.mode = color_sensor_mode
        self.__ir = InfraredSensor()
        self.__ir.mode = infra_sensor_mode

    def __turn_left(self):
        self.__movesteering.on(-50, 30)

    def __turn_right(self):
        self.__movesteering.on(50, 30)

    def __run_forward(self):
        self.__movesteering.on(0, 50)

    def __run_backward(self):
        self.__movesteering.on(0, -20)

    def __stop(self):
        self.__movesteering.off()

    def __play_text_sound(self, words):
        sound = Sound()
        sound.speak(words)

    def __lift_up(self):
        self.__mediummotor.on_for_degrees(10, 50)

    def __lift_down(self):
        self.__mediummotor.on_for_degrees(10, -50)

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
        elif(button_value == 2):
            self.__lift_up()
        elif(button_value == 4):
            self.__lift_down()
        # elif(button_value == 2):
        #     self.__play_text_sound("Lily, I love you")
        else:
            self.__stop()

    def __color_detect(self):
        color = self.__cs.color
        if(color == 1):
            self.__play_text_sound("black")
        elif(color == 2):
            self.__play_text_sound("blue")
        elif(color == 3):
            self.__play_text_sound("green")
        elif(color == 4):
            self.__play_text_sound("yellow")
        elif(color == 5):
            self.__play_text_sound("red")
        elif(color == 6):
            self.__play_text_sound("white")
        elif(color == 7):
            self.__play_text_sound("brown")
        else:
            pass


    def process(self):
        self.__ir.process()
        buttons_pressed = self.__ir.buttons_pressed()
        button_value = self.__get_button_pressed_value(buttons_pressed)
        self.__run(button_value)
        self.__color_detect()