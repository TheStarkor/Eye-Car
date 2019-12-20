import picamera
import time

camera = picamera.PiCamera()
camera.resolution=(1920,1080)

camera.start_preview()
time.sleep(20)
# camera.capture('./t2.jpg')
camera.stop_preview()
