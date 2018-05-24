import colordef as cd
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as npimg

# face: 0- left side of picture. 1- right side of picture
def getFace(img,face,pixel,array):
    array = numpy.zeros(shape=(3,3))
    if face ==  0:
        array[0][0] = cd.getColor(img,pixel[0])
        array[0][1] = cd.getColor(img,pixel[1])
        array[0][2] = cd.getColor(img,pixel[2])
        array[1][0] = cd.getColor(img,pixel[3])
        array[1][1] = cd.getColor(img,pixel[4])
        array[1][2] = cd.getColor(img,pixel[5])
        array[2][0] = cd.getColor(img,pixel[6])
        array[2][1] = cd.getColor(img,pixel[7])
        array[2][2] = cd.getColor(img,pixel[8])
    else:
        array[0][0] = cd.getColor(img,pixel[9])
        array[0][1] = cdgetColor(img,pixel[10])
        array[0][2] = cd.getColor(img,pixel[11])
        array[1][0] = cd.getColor(img,pixel[12])
        array[1][1] = cd.getColor(img,pixel[13])
        array[1][2] = cd.getColor(img,pixel[14])
        array[2][0] = cd.getColor(img,pixel[15])
        array[2][1] = cd.getColor(img,pixel[16])
        array[2][2] = cd.getColor(img,pixel[17])
    return array
// Orientation of Master Rubix Cube Array containing faces           
def getOrientation(face,array):
    if face[1][1] == 'White':
        array[0] = face;
    else if face[1][1] == 'Green':
        array[1] = face;
    else if face[1][1] == 'Orange':
        array[2] = face;
    else if face[1][1] == 'Blue':
        array[3] = face;
    else if face[1][1] == 'Red':
        array[4] = face;
    else if face[1][1] === 'Yellow':
        array[5] = face;
    return array;


