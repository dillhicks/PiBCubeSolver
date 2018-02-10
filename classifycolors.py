import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as npimg
#approximate color codes for cube
CUBE_COLORS = {"Red":(255,0,0), "Yellow":(237,167,16), "Green":(13,186,47), "White":(255,255,255), "Orange":(255,144,0), "Blue":(0,0,255)} 

def colordiff(color1, color2):
	return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])



def classcolor(mycolor):
	differences = [[colordiff(mycolor, targetvalue), targetname] for targetname, targetvalue in CUBE_COLORS.items()]
	differences.sort() 
	mycolorname = differences[0][1]
	return mycolorname




#colortest = (255,255,0)
#colorname = classcolor(colortest)
#print(colorname)
