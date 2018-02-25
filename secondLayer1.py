import numpy as np
import faceRotation.py

# These functions depend on a constant orientation
def topToRightRed():
    rotateTop();
    rotateRight()
    rotateCCTop()
    rotateCCRight()
    rotateFront()
    rotateCCRight()
    rotateCCFront()
    rotateRight()
def topToLeftRed():
    rotateCCTop()
    rotateCCLeft()
    rotateTop()
    rotateLeft()
    rotateCCFront()
    rotateLeft()
    rotateFront()
    rotateCCLeft()
def topToRightBlue():
    rotateTop()
    rotateFront()
    rotateCCTop()
    rotateCCFront()
    rotateLeft()
    rotateCCFront()
    rotateCCLeft()
    rotateFront()
def topToLeftBlue():
    rotateCCTop()
    rotateCCBack()
    rotateTop()
    rotateBack()
    rotateCCLeft()
    rotateBack()
    rotateLeft()
    rotateCCBack()
def topToRightGreen():
    rotateTop()
    rotateBack()
    rotateCCTop()
    rotateCCBack()
    rotateRight()
    rotateCCBack()
    rotateCCRight()
    rotateBack()
def topToLeftGreen():
    rotateCCTop()
    rotateCCFront()
    rotateTop()
    rotateFront()
    rotateCCRight()
    rotateFront()
    rotateRight()
    rotateCCFront()
# Or Pink depending on your Rubix Cube
def topToRightOrange():
    rotateTop()
    rotateLeft()
    rotateCCTop()
    rotateCCLeft()
    rotateBack()
    rotateCCLeft()
    rotateCCBack()
    rotateLeft()
def topToLeftOrange():
    rotateCCTop()
    rotateCCRight()
    rotateTop()
    rotateRight()
    rotateCCBack() 
    rotateRight()
    rotateBack()
    rotateCCRight()

def secondLayerComplete():
    if(top[2][1] == left[1][1]):
        topToLeftRed()
    elif(top[2][1] == right[1][1]):
        topToRightRed()
    if(top[1][0] == back[1][1]):
        topToLeftBlue()
    elif(top[1][0] == front[1][1]):
        topToRightBlue()
    if(top[1][2] == front[1][1]):
        topToLeftGreen()
    elif(top[1][2] == back[1][1]):
        topToRightGreen()
    if(top[0][1] == right[1][1]):
        topToLeftOrange()
    elif(top[0][1] == left[1][1]):
        topToRightOrange()


        

