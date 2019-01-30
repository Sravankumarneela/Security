import RPi.GPIO as gpio
import time

class gate:

    def __init__(self):
        self.m11 = 13
        gpio.setmode(gpio.BCM)
        gpio.setup(self.m11, gpio.OUT)
        self.p=gpio.PWM(self.m11,50)
        self.p.start(0)


    def open_gate(self):
        self.p.ChangeDutyCycle(7)
        time.sleep(1)


    def close_gate(self):
        self.p.ChangeDutyCycle(0)
        time.sleep(1)




