import cv2
import numpy as np 
import maplotlib.pyplot as plt 
import matplotlib.image as npimg
from picamera.array import PiRGBArray
from picamera import PiCamera
import time


#TODO update colors and pixel files 
CUBE_COLORS = {"R":(255,0,0), "Y":(237,167,16), "G":(13,186,47), "W":(255,255,255), "O":(255,144,0), "B":(0,0,255)} 
CUBE_PIXELS_L = [[,,,], #left(side) top (row) left (column)
				[,,,],  #left top center
				[,,,],  #left top right
				[,,,],  #left center left
				[,,,],  #left center center
				[,,,],  #left center right
				[,,,],  #left bottom left
				[,,,],  #left bottom center
				[,,,] ] #left bottom right

CUBE_PIXELS_R = [[,,,], #right top left
				[,,,],  #right top center
				[,,,],  #right top right
				[,,,],  #right center left
				[,,,],  #right center center
				[,,,],  #right center right
				[,,,],  #right bottom left
				[,,,],  #right bottom center
				[,,,] ] #right bottom right

def take_picture():
	camera = PiCamera()
	rawCapture = PiRGBArray(camera)
	time.sleep(0.1)
	camera.capture(rawCapture, format = "bgr")
	img = rawCapture.array
	return img

def color_diff(color1, color2):
	return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])

def class_color(color):
	differences = [[color_diff(color, targetvalue), targetname] for targetname, targetvalue in CUBE_COLORS.items()]
	differences.sort() 
	color_name = differences[0][1]
	return color_name

def get_color(img, pixel):
	pixels = img[pixel[0]:pixel[1], pixel[2]:pixel[3]]
	acpr = np.average(pixels, axis = 0)
	ac = np.average(acpr, axis = 0)
	color_name = class_color(ac)
	return color_name

def init_scan():
	img = take_picture() 
	f1 = np.zeros(shape = (3,3)) #left face
	f2 = np.zeros(shape = (3,3)) #right face
	x,y = 0 
	for pixels in CUBE_PIXELS_L:
		color = get_color(img, pixels)
		if x == 3:
			x = 0
			y++  
		f1[x][y] = color
		x++
	x,y = 0
	for pixels in CUBE_PIXELS_R:
		color = get_color(img,pixels)
		if x = 3:
			x = 0
			y++  
		f1[x][y] = color
		x++
	return f1, f2