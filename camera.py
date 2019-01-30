import time
import picamera


class Camera:

    data = time.strftime("%d_%b_%Y/%H:%M:%S")

    def __init__(self):
        pass

    def capture_image(self):
        picamera.start_preview()
        time.sleep(5)
        picamera.capture('/home/pi/Desktop/Visitors/%s.jpg' % self.data)
        picamera.stop_preview()
