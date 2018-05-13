from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2

def cameraArray():
	#using rpi camera to make array to be used in rpi 
	camera = PiCamera()
	camera.resolution = (1920, 1080)
	camera.start_preview()
	sleep(3)
	camera.stop_preview()
	with picamera.array.PiRGBArray(camera) as stream:
        camera.capture(stream, format='bgr')
        image = stream.array
    cv2.imshow("OpenCV Test", image)
    cv2.waitkey(0)
    cv2.destroyAllWindows(0)

	

cameraArray()