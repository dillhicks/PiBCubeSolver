import cv2
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as npimg

def color_diff(color1, color2):
	return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])

def class_color(color):
	differences = [[color_diff(color, targetvalue), targetname] for targetname, targetvalue in CUBE_COLORS.items()]
	differences.sort() 
	color_name = differences[0][1]
	if color_name == "BB":
		return "B"
	if color_name == "BR":
		return"R"
	else:
		return color_name

def get_color(img, pixel):
	pixels = img[pixel[0]:pixel[1], pixel[2]:pixel[3]]
	#imgplot = plt.imshow(pixels)
	#plt.show()
	acpr = np.average(pixels, axis = 0)
	ac = np.average(acpr, axis = 0)
	color_name = class_color(ac)
	return color_name

def get_rgb(img,pixel):
	pixels = img[pixel[0]:pixel[1], pixel[2]:pixel[3]]
	#imgplot = plt.imshow(pixels)
	#plt.show()
	acpr = np.average(pixels, axis = 0)
	ac = np.average(acpr, axis = 0)
	return ac

pixelarray_l=	[#LEFT 
				[400,510,690,750],
				[750,850,690,750],
				[1020,1060,690,750],
				

				[400,510,843,964],
				[750,840,860,930],
				[1240,1290, 840, 950],


				[400,510,1080,1180],
				[800,900,1080,1180],
				[1300, 1350, 1070, 1180]
				]

				#RIGHT
pixelarray_r= 	[[400,510,1340,1440],
				[750,850,1340,1440],
				[1200,1300,1340,1440],

				[400,500,1650, 1720],
				[750,850,1650, 1720],
				[1150,1250,1650, 1720],

				[450,550,1860, 1920],
				[750,850,1860, 1920],
				[1110,1200,1860, 1920],]



left_colors = []
right_colors = []

CUBE_COLORS = {"R":(123,32,40), "BR": (160,70,70), "Y":(167,138,58), "G":(13,90,3), "W":(125,141,150), "O":(181,73,15), "B":(59,101,155), "BB":(80,100,150)} 


img = cv2.imread("img1.jpg")
npimg = npimg.imread('img1.jpg')

for pixelset in pixelarray_l:
	cv2.rectangle(img, (pixelset[2],pixelset[0]), (pixelset[3],pixelset[1]), (255,0,0),2)
	left_colors.append(get_rgb(npimg, pixelset))
	print(get_color(npimg, pixelset))
 
for pixelset in pixelarray_r:
	cv2.rectangle(img, (pixelset[2],pixelset[0]), (pixelset[3],pixelset[1]), (255,0,0),2)
	right_colors.append(get_rgb(npimg, pixelset))
	print(get_color(npimg, pixelset))

np_left = np.array(left_colors)
np_right = np.array(right_colors)

print("left:")
for color in left_colors:
	print str(color) + "n"
print("right:")
for color in right_colors:
	print str(color) + "n"

print("left:")
print(np_left.mean(axis=0))	
print("right:")
print(np_right.mean(axis=0))	



img = cv2.resize(img, (0,0), fx=0.25, fy=0.25) 
cv2.imshow("image", img)
q = cv2.waitKey(0)