from dashboard.Digit import Digit
import math
from dashboard.Component import Component

class SpeedDigits(Component):
    def __init__(self, window, position0=(50, 50), position1=(210, 50), segment_length=100, segment_width=15):
        self.window = window
        self.position0 = position0
        self.position1 = position1
        self.segment_length = segment_length
        self.segment_width = segment_width
        
        self.digit_display0 = Digit(self.window, position0)
        self.digit_display1 = Digit(self.window, position1)

    def set_speed(self, speed):
        if 0 <= speed < 100:
            tens = math.floor(speed/10)
            ones = speed % 10
            self.digit_display0.set_digit(tens)
            self.digit_display1.set_digit(ones)
        else:
            raise ValueError("Speed must be between 0 and 99.")

    def display(self):
        self.digit_display0.display()
        self.digit_display1.display()
