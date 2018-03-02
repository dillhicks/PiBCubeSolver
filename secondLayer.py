import numpy as np
import printFaces as pf
#import faceRotation as fr
import faceRotation as fr
y = 'y'
w = 'w'
g = 'g'
b = 'b'
r = 'r'
o = 'o'

# Test arrays
#top = np.array( [[y,y,y],[y,y,y],[y,y,y]] )
#bottom = np.array( [[w,w,w],[w,w,w],[w,w,w]] )
#right = np.array( [[o,o,o],[g,g,g],[g,g,g]] )
#left = np.array( [[r,r,r],[b,b,b], [b,b,b]] )
#front = np.array( [[g,g,g],[r,r,r],[r,r,r]] )
#back = np.array( [[o,o,o],[o,o,o],[b,b,b]] )

# Master array
#cube = np.array( [bottom,right,back,left,front,top] )

def topLayerAlign( cube ):
   import faceRotation as fr
   #print "Hello"
   # Check if the middle layer is filled
   midLayerCheck = 0
   # Check if mid green layer is filled
   if( cube[1][1][0] == 'g' and cube[1][1][1] == 'g' and cube[1][1][2] == 'g' ):
      midLayerCheck+= 1
   # Check if mid orange layer is filled
   if( cube[2][1][0] == 'o' and cube[2][1][1] == 'o' and cube[2][1][2] == 'o' ):
      midLayerCheck+= 1
   # Check if mid blue layer is filled
   if( cube[3][1][0] == 'b' and cube[3][1][1] == 'b' and cube[3][1][2] == 'b' ):
      midLayerCheck+= 1
   # Check if mid red layer is filled   
   if( cube[4][1][0] == 'r' and cube[4][1][1] == 'r' and cube[4][1][2] == 'r' ):
      midLayerCheck+= 1
   
   # If middle layer is filled end method
   if( midLayerCheck == 4 ):
      print "Hello"
      return 
   
   #print "doesnt work"
   
   
   # Check if green side has a T
   if( cube[1][0][1] == 'g' and cube[5][1][2] != 'y' ):
      return

   # Check if the orange side has a T
   if( cube[2][2][1] == 'o' and cube[5][0][1] != 'y' ):
      return

   # Check if the blue side has a T
   if( cube[3][0][1] == 'b' and cube[5][1][0] != 'y' ):
      return

   # Check if the red side has a T
   if( cube[4][0][1] == 'r' and cube[5][2][1] != 'y' ):
      return


   # Check if green side has a red piece at the top mid
   if( cube[1][0][1] == 'r' and cube[5][1][2] != 'y' ):
      # rotate top clockwise from green side
      fr.cube1 = fr.rotateTop()
      return
   
   # Check if green side has a blue piece
   if( cube[1][0][1] == 'b' and cube[5][1][2] != 'y' ):
      fr.cube1 = fr.rotateTop()
      fr.cube1 = fr.rotateTop()
      return

   # Check if the green side has a orange piece
   if( cube[1][0][1] == 'o' and cube[5][1][2] != 'y' ):
      fr.cube1 = fr.rotateCCTop()
      return

   #----------------------------------------------
   #  Check if orange side has different color piece
   
   if( cube[2][2][1] == 'r' and cube[5][0][1] != 'y' ):
      fr.cube1 = fr.rotateTop()
      fr.cube1 = fr.rotateTop()
      return

   if( cube[2][2][1] == 'b' and cube[5][0][1] != 'y' ):
      fr.cube1 = fr.rotateCCTop()
      return

   if( cube[2][2][1] == 'g' and cube[5][0][1] != 'y' ):
      fr.cube1 = fr.rotateTop()
      return
  #------------------------------------------------
   #  Check if blue side has different color piece

   if( cube[3][0][1] == 'r' and cube[5][1][0] != 'y' ):
      fr.cube1 = rotateCCTop()
      return

   if( cube[3][0][1] == 'g' and cube[5][1][0] != 'y' ):
      fr.cube1 = fr.rotateTop()
      fr.cube1 = fr.rotateTop()
      return
   
   if( cube[3][0][1] == 'o' and cube[5][1][0] != 'y' ):
      fr.cube1 = fr.rotateTop()
      return
   
   #-------------------------------------------------
   #  Check if red side has different color piece

   if( cube[4][0][1] == 'b' and cube[5][2][1] != 'y' ):
      fr.cube1 = fr.rotateTop()
      return
   
   if( cube[4][0][1] == 'g' and cube[5][2][1] != 'y' ):
      fr.cube1 = fr.rotateCCTop()
      return

   if( cube[4][0][1] == 'o' and cube[5][2][1] != 'y' ):
      fr.cube1 = fr.rotateTop()
      fr.cube1 = fr.rotateTop()
      return
   


# These functions depend on a constant orientation
def topToRightRed():
    fr.rotateTop();
    fr.rotateRight()
    fr.rotateCCTop()
    fr.rotateCCRight()
    fr.rotateFront()
    fr.rotateCCRight()
    fr.rotateCCFront()
    fr.rotateRight()
def topToLeftRed():
    fr.rotateCCTop()
    fr.rotateCCLeft()
    fr.rotateTop()
    fr.rotateLeft()
    fr.rotateCCFront()
    fr.rotateLeft()
    fr.rotateFront()
    fr.rotateCCLeft()
def topToRightBlue():
    fr.rotateTop()
    fr.rotateFront()
    fr.rotateCCTop()
    fr.rotateCCFront()
    fr.rotateLeft()
    fr.rotateCCFront()
    fr.rotateCCLeft()
    fr.rotateFront()
def topToLeftBlue():
    fr.rotateCCTop()
    fr.rotateCCBack()
    fr.rotateTop()
    fr.rotateBack()
    fr.rotateCCLeft()
    fr.rotateBack()
    fr.rotateLeft()
    fr.rotateCCBack()
def topToRightGreen():
    fr.rotateTop()
    fr.rotateBack()
    fr.rotateCCTop()
    fr.rotateCCBack()
    fr.rotateRight()
    fr.rotateCCBack()
    fr.rotateCCRight()
    fr.rotateBack()
def topToLeftGreen():
    fr.rotateCCTop()
    fr.rotateCCFront()
    fr.rotateTop()
    fr.rotateFront()
    fr.rotateCCRight()
    fr.rotateFront()
    fr.rotateRight()
    fr.rotateCCFront()
# Or Pink depending on your Rubix Cube
def topToRightOrange():
    fr.rotateTop()
    fr.rotateLeft()
    fr.rotateCCTop()
    fr.rotateCCLeft()
    fr.rotateBack()
    fr.rotateCCLeft()
    fr.rotateCCBack()
    fr.rotateLeft()
def topToLeftOrange():
    fr.rotateCCTop()
    fr.rotateCCRight()
    fr.rotateTop()
    fr.rotateRight()
    fr.rotateCCBack() 
    fr.rotateRight()
    fr.rotateBack()
    fr.rotateCCRight()

def secondLayerComplete(cube):
    if(cube[4][1][1] == cube[4][0][1]):
      print "Red side"
      if(cube[5][2][1] == cube[3][1][1]):
         topToLeftRed()
      elif(cube[5][2][1] == cube[1][1][1]):
         topToRightRed()
    if(cube[3][1][1] == cube[3][0][1]):
      print "Blue side"
      if(cube[5][1][0] == cube[2][1][1]):
         topToLeftBlue()
      elif(cube[5][1][0] == cube[4][1][1]):
         topToRightBlue()
    if(cube[1][1][1] == cube[1][0][1]):
      print "Green side"
      if(cube[5][1][2] == cube[4][1][1]):
         topToLeftGreen()
      elif(cube[5][1][2] == cube[2][1][1]):
         topToRightGreen()
    if(cube[2][1][1] == cube[2][2][1]):
      print "Orange"
      if(cube[5][0][1] == cube[1][1][1]):
         topToLeftOrange()
      elif(cube[5][0][1] == cube[3][1][1]):
         topToRightOrange()
    pf.printFaces(cube)

def solveSecondLayer(cube): 
   print "in"
 #  a = 1
 #  b = 2
 #  while( (a < 1) 
 #     and (b < 5)):
 #     print "infinite"
 #     a = a + 1
 #     b = b + 1
   
   secondLayerCheck = 0
   
   # Check if mid green layer is filled
   if( cube[1][1][0] == 'g' and cube[1][1][1] == 'g' and cube[1][1][2] == 'g' ):
      secondLayerCheck+= 1
   # Check if mid orange layer is filled
   if( cube[2][1][0] == 'o' and cube[2][1][1] == 'o' and cube[2][1][2] == 'o' ):
      secondLayerCheck+= 1
   # Check if mid blue layer is filled
   if( cube[3][1][0] == 'b' and cube[3][1][1] == 'b' and cube[3][1][2] == 'b' ):
      secondLayerCheck+= 1
   # Check if mid red layer is filled   
   if( cube[4][1][0] == 'r' and cube[4][1][1] == 'r' and cube[4][1][2] == 'r' ):
      secondLayerCheck+= 1
   

   
   while( secondLayerCheck != 4 ):
      secondLayerCheck = 0
      # Check if mid green layer is filled
      if( cube[1][1][0] == 'g' and cube[1][1][1] == 'g' and cube[1][1][2] == 'g' ):
         secondLayerCheck+= 1
      # Check if mid orange layer is filled
      if( cube[2][1][0] == 'o' and cube[2][1][1] == 'o' and cube[2][1][2] == 'o' ):
         secondLayerCheck+= 1
      # Check if mid blue layer is filled
      if( cube[3][1][0] == 'b' and cube[3][1][1] == 'b' and cube[3][1][2] == 'b' ):
         secondLayerCheck+= 1
      # Check if mid red layer is filled   
      if( cube[4][1][0] == 'r' and cube[4][1][1] == 'r' and cube[4][1][2] == 'r' ):
         secondLayerCheck+= 1
   
      topLayerAlign(cube)
      secondLayerComplete(cube)
      pf.printFaces(cube) 
