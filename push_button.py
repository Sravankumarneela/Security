import RPi.GPIO as gpio
import camera
import lcd
import time
a = camera.Camera()
b = lcd.Lcd_Dnhndghnisplay()


class Push:


    def __init__(self):
        self.button = 19
        self.status = 1
        self.led = 5
        self.buz = 6
        gpio.setmode(gpio.BCM)
        for x in (self.buz,self.led):
            gpio.setup(x, gpio.OUT)
        gpio.setup(self.button, gpio.IN)
        gpio.output(self.buz,0)
        gpio.output(self.led,1)


    def pressed(self):
        self.status = 0
        b.please_wait()
        b.readytocapture()
        time.sleep(5)
        a.capture_image()
        b.image_captured()
        self.status = 1



