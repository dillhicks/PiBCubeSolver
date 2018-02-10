
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as npimg


def getFace(img,face,pixel):
    array = numpy.zeros(shape=(3,3))
    if face ==  0:
        array[0][0] = getColor(img,pixel[0])
        array[0][1] = getColor(img,pixel[1])
        array[0][2] = getColor(img,pixel[2])
        array[1][0] = getColor(img,pixel[3])
        array[1][1] = getColor(img,pixel[4])
        array[1][2] = getColor(img,pixel[5])
        array[2][0] = getColor(img,pixel[6])
        array[2][1] = getColor(img,pixel[7])
        array[2][2] = getColor(img,pixel[8])
    else:
        array[0][0] = getColor(img,pixel[9])
        array[0][1] = getColor(img,pixel[10])
        array[0][2] = getColor(img,pixel[11])
        array[1][0] = getColor(img,pixel[12])
        array[1][1] = getColor(img,pixel[13])
        array[1][2] = getColor(img,pixel[14])
        array[2][0] = getColor(img,pixel[15])
        array[2][1] = getColor(img,pixel[16])
        array[2][2] = getColor(img,pixel[17])
    return array
           
        

