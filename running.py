import push_button
import RPi.GPIO as gpio
import time
import motor


a = push_button.Push()
b = motor.gate()

while 1:
    if gpio.input(a.button) == 0 and a.status == 1:
        gpio.output(a.led, 0)
        gpio.output(a.buz, 1)
        time.sleep(1)
        gpio.output(a.buz, 0)
        a.pressed()
        b.open_gate()
        time.sleep(15)
        b.close_gate()
        time.sleep(1)
        gpio.output(a.led, 1)

