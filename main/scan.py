import cv2
import numpy
import maplotlib.pyplot as plt 
import matplotlib.image as npimg
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

CUBE_COLORS = {"Red":(255,0,0), "Yellow":(237,167,16), "Green":(13,186,47), "White":(255,255,255), "Orange":(255,144,0), "Blue":(0,0,255)} 
CUBE_PIXELS = [ [,,,],  #left(side) top (row) left (column)
				[,,,],  #left top center
				[,,,],  #left top right
				[,,,],  #left center left
				[,,,],  #left center center
				[,,,],  #left center right
				[,,,],  #left bottom left
				[,,,],  #left bottom center
				[,,,],  #left bottom right
				[,,,],  #right top left
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

def init_scan():
	take_picture()











	return f1, f2