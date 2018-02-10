import cv2
import numpy as np
import matplotlib.pyplot as plt
import classifycolors as cp
#rom picamera.array import PiRGBArray
#from picamera import PiCamera

'''
#function for taking an image when the camera arrives
def takepicture():
	camera = PiCamera()
	rawCapture = PiRGBArray(camera)
	camera.capture(rawCapture, format = "rgb")
	image = rawCapture.array
	return image
'''

def getcolor(img,pixel): 
	center = img[pixel[0]:pixel[1], pixel[2]:pixel[3]]
	acpr = np.average (center, axis = 0)
	ac = np.average(acpr, axis = 0)
	colorname = cp.classcolor(ac)
	return colorname 



#1460:1620, 1000:1200  green
#600:1000, 2200:2600 yellow
#1800:2400, 1800:2400 red
pixel = [ [1460,1620,1000,1200], [600,1000,2200,2600], [1800,2400,1800,2400] ]
image = cv2.imread('cornerimg.JPG')
imagec = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
colortest = getcolor(imagec,pixel[2])
print(colortest)
