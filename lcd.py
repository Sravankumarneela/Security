import Adafruit_CharLCD as LCD

lcd_rs = 12
lcd_en = 16
lcd_d4 = 18
lcd_d5 = 36
lcd_d6 = 38
lcd_d7 = 40
lcd_backlight = 2
lcd_columns = 16
lcd_rows = 2


class Lcd_Display:

    def __init__(self):
        self.lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

    def please_wait(self):
        self.lcd.clear()
        self.lcd.message('please wait')

    def image_captured(self):
        self.lcd.clear()
        self.lcd.message('image captured')
        self.lcd.set_cursor(1,0)
        self.lcd.message('THANK YOU')

    def readytocapture(self):
        self.lcd.clear()
        self.lcd.message('READY TO CAPTURE')
        time.sleep(5)
        self.lcd.clear()
        self.lcd.message('CAPTURING')


