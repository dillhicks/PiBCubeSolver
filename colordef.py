import cv2
import numpy as np
import matplotlib.pyplot as plt
import classifycolors as cp
#rom picamera.array import PiRGBArray
#from picamera import PiCamera


#function for taking an image when the camera arrives
def takePicture():
	camera = PiCamera()
    camera.resolution = (1920,1080)
    camera.start_preview()
    sleep(3)
    camera.stop_preview()
    with picamera.array.PiRGBArray(camera) as stream:
        camera.capture(stream, format = "rgb")
		camera.capture(rawCapture, format = "rgb")
        image = stream.array
	cv2.imshow("OpenCV Test", image)
    cv2.waitkey(0)
    cv2.destroyAllWindows(0)
	return image

def getcolor(img,pixel): 
	center = img[pixel[0]:pixel[1], pixel[2]:pixel[3]]
	acpr = np.average (center, axis = 0)
	ac = np.average(acpr, axis = 0)
	colorname = cp.classcolor(ac)
	return colorname 


takePicture()
#TODO: setup pixel array
pixel = [ [1460,1620,1000,1200], [600,1000,2200,2600], [1800,2400,1800,2400] ]

imagec = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
colortest = getcolor(imagec,pixel[2])
print(colortest)
