import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
 
img = cv2.imread('cornerimgresized.JPG')

boundaries = [ #these are BGR values
	([85, 150, 15], [150, 190, 100]), #green 
	([0, 0, 71], [45, 70, 160]), #red 
	([0, 110, 160], [15, 174, 250]), #yellow
]

def detectColors():
	for (lower, upper) in boundaries:
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		mask = cv2.inRange(img, lower, upper)
		output = cv2.bitwise_and(img, img, mask = mask)

		cv2.imshow("red detection", np.hstack([img, output]))
		cv2.waitKey(0)

detectColors()
"""
plotimage = mpimg.imread('cornerimgresized.JPG')
imgplot = plt.imshow(plotimage)
plt.show()
"""