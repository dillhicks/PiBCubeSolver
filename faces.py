import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as npimg
from picamera.array import PiRGBArray
from picamera import PiCamera


#function for taking an image when the camera arrives
def takepicture():
	camera = PiCamera()
	rawCapture = PiRGBArray(camera)
	camera.capture(rawCapture, format = "rgb")
	image = rawCapture.array
	return image

#function for getting RGB Average of First Center
def center1(imgfile): #imgfile = image file, pixels = wanted pixel array
	#read image and convert to RGB
	img = cv2.imread(imgfile)
	imgc = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

	#find and return center color	
	center = imgc[1460:1620, 1000:1200]
	acpr = np.average(center, axis = 0)
	ac = np.average(acpr,axis = 0)
	return ac

#function for getting RGB Average of Second Center
def center2(imgfile):
#read image and convert to RGB
	img = cv2.imread(imgfile)
	imgc = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

	#find and return center color	
	center = imgc[800:920, 2050:2250]
	acpr = np.average(center, axis = 0)
	ac = np.average(acpr,axis = 0)
	return ac

#function for getting RGB Average of Second Center
def center3(imgfile):
	#read image and convert to RGB
	img = cv2.imread(imgfile)
	imgc = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

	#find and return center color	
	center = imgc[2120:2180, 2150:2300]
	acpr = np.average(center, axis = 0)
	ac = np.average(acpr,axis = 0)
	return ac


#plt.imshow(center3)
#plt.show()








