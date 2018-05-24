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

def topLayerAlign():
   print "Aligning top layer"
   print "------------------"
   
   topLayerYellowCheck = 0
   if( fr.cube1[1][0][1] == 'y' or fr.cube1[5][1][2] == 'y' ):
      #print "green"
      topLayerYellowCheck+= 1
   if( fr.cube1[2][2][1] == 'y' or fr.cube1[5][0][1] == 'y' ):
      #print "orange"
      topLayerYellowCheck+= 1
   if( fr.cube1[3][0][1] == 'y' or fr.cube1[5][1][0] == 'y' ):
      #print "blue"
      topLayerYellowCheck+= 1
   if( fr.cube1[4][0][1] == 'y' or fr.cube1[5][2][1] == 'y' ):
      #print "red"
      topLayerYellowCheck+= 1
   
   #print topLayerYellowCheck
   if( topLayerYellowCheck == 4 ):
      topToRightRed()
      return

   
   # Check if the middle layer is filled
   midLayerCheck = 0
   # Check if mid green layer is filled
   if( fr.cube1[1][1][0] == 'g' and fr.cube1[1][1][1] == 'g' and fr.cube1[1][1][2] == 'g' ):
      midLayerCheck+= 1
   # Check if mid orange layer is filled
   if( fr.cube1[2][1][0] == 'o' and fr.cube1[2][1][1] == 'o' and fr.cube1[2][1][2] == 'o' ):
      midLayerCheck+= 1
   # Check if mid blue layer is filled
   if( fr.cube1[3][1][0] == 'b' and fr.cube1[3][1][1] == 'b' and fr.cube1[3][1][2] == 'b' ):
      midLayerCheck+= 1
   # Check if mid red layer is filled   
   if( fr.cube1[4][1][0] == 'r' and fr.cube1[4][1][1] == 'r' and fr.cube1[4][1][2] == 'r' ):
      midLayerCheck+= 1
   
   # If middle layer is filled end method
   if( midLayerCheck == 4 ):
      return 
   
   #print "doesnt work"
   
   
   # Check if green side has a T
   if( fr.cube1[1][0][1] == 'g' and fr.cube1[5][1][2] != 'y' ):
      return

   # Check if the orange side has a T
   if( fr.cube1[2][2][1] == 'o' and fr.cube1[5][0][1] != 'y' ):
      return

   # Check if the blue side has a T
   if( fr.cube1[3][0][1] == 'b' and fr.cube1[5][1][0] != 'y' ):
      return

   # Check if the red side has a T
   if( fr.cube1[4][0][1] == 'r' and fr.cube1[5][2][1] != 'y' ):
      return
   


   # Check if green side has a red piece at the top mid
   if( fr.cube1[1][0][1] == 'r' and fr.cube1[5][1][2] != 'y' ):
      # rotate top clockwise from green side
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      return
   
   # Check if green side has a blue piece
   if( fr.cube1[1][0][1] == 'b' and fr.cube1[5][1][2] != 'y' ):
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      return

   # Check if the green side has a orange piece
   if( fr.cube1[1][0][1] == 'o' and fr.cube1[5][1][2] != 'y' ):
      fr.cube1 = fr.rotateCCTop()
      pf.printFaces(fr.cube1)
      return

   #----------------------------------------------
   #  Check if orange side has different color piece
   
   if( fr.cube1[2][2][1] == 'r' and fr.cube1[5][0][1] != 'y' ):
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      return

   if( fr.cube1[2][2][1] == 'b' and fr.cube1[5][0][1] != 'y' ):
      fr.cube1 = fr.rotateCCTop()
      pf.printFaces(fr.cube1)
      return

   if( fr.cube1[2][2][1] == 'g' and fr.cube1[5][0][1] != 'y' ):
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      return
  #------------------------------------------------
   #  Check if blue side has different color piece

   if( fr.cube1[3][0][1] == 'r' and fr.cube1[5][1][0] != 'y' ):
      fr.cube1 = fr.rotateCCTop()
      pf.printFaces(fr.cube1)
      return

   if( fr.cube1[3][0][1] == 'g' and fr.cube1[5][1][0] != 'y' ):
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      return
   
   if( fr.cube1[3][0][1] == 'o' and fr.cube1[5][1][0] != 'y' ):
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      return
   
   #-------------------------------------------------
   #  Check if red side has different color piece

   if( fr.cube1[4][0][1] == 'b' and fr.cube1[5][2][1] != 'y' ):
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      return
   
   if( fr.cube1[4][0][1] == 'g' and fr.cube1[5][2][1] != 'y' ):
      fr.cube1 = fr.rotateCCTop()
      pf.printFaces(fr.cube1)
      return

   if( fr.cube1[4][0][1] == 'o' and fr.cube1[5][2][1] != 'y' ):
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      fr.cube1 = fr.rotateTop()
      pf.printFaces(fr.cube1)
      return
   #print "Heya"
   return


# These functions depend on a constant orientation
def topToRightRed():
    print "top to right"
    fr.cube1 = fr.rotateTop()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateRight() 
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCTop()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCRight()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateFront()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCRight()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCFront()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateRight()
    pf.printFaces(fr.cube1)

def topToLeftRed():
    print "top to left"
    fr.cube1 = fr.rotateCCTop()
    fr.cube1 = fr.rotateCCLeft()
    fr.cube1 = fr.rotateTop()
    fr.cube1 = fr.rotateLeft()
    fr.cube1 = fr.rotateCCFront()
    fr.cube1 = fr.rotateLeft()
    fr.cube1 = fr.rotateFront()
    fr.cube1 = fr.rotateCCLeft()
    pf.printFaces(fr.cube1)
def topToRightBlue():
    print "top to right"
    fr.cube1 = fr.rotateTop()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateFront()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCTop()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCFront()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateLeft()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCFront()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCLeft()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateFront()
    pf.printFaces(fr.cube1)
def topToLeftBlue():
    print "top to left"
    fr.cube1 = fr.rotateCCTop()
    fr.cube1 = fr.rotateCCBack()
    fr.cube1 = fr.rotateTop()
    fr.cube1 = fr.rotateBack()
    fr.cube1 = fr.rotateCCLeft()
    fr.cube1 = fr.rotateBack()
    fr.cube1 = fr.rotateLeft()
    fr.cube1 = fr.rotateCCBack()
    pf.printFaces(fr.cube1)
def topToRightGreen():
    print "top to right"
    fr.cube1 = fr.rotateTop()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateBack()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCTop()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCBack()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateRight()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCBack()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCRight()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateBack()
    pf.printFaces(fr.cube1)
def topToLeftGreen():
    print "top to left"
    fr.cube1 = fr.rotateCCTop()
    fr.cube1 = fr.rotateCCFront()
    fr.cube1 = fr.rotateTop()
    fr.cube1 = fr.rotateFront()
    fr.cube1 = fr.rotateCCRight()
    fr.cube1 = fr.rotateFront()
    fr.cube1 = fr.rotateRight()
    fr.cube1 = fr.rotateCCFront()
    pf.printFaces(fr.cube1)
# Or Pink depending on your Rubix Cube
def topToRightOrange():
    print "top to right"
    fr.cube1 = fr.rotateTop()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateLeft()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCTop()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCLeft()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateBack()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCLeft()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateCCBack()
    #pf.printFaces(fr.cube1)
    fr.cube1 = fr.rotateLeft()
    pf.printFaces(fr.cube1)
def topToLeftOrange():
    print "top to left"
    fr.cube1 = fr.rotateCCTop()
    fr.cube1 = fr.rotateCCRight()
    fr.cube1 = fr.rotateTop()
    fr.cube1 = fr.rotateRight()
    fr.cube1 = fr.rotateCCBack() 
    fr.cube1 = fr.rotateRight()
    fr.cube1 = fr.rotateBack()
    fr.cube1 = fr.rotateCCRight()
    pf.printFaces(fr.cube1)
def secondLayerComplete():
    if(fr.cube1[4][1][1] == fr.cube1[4][0][1] and fr.cube1[5][2][1] != 'y'):
      print "Red side"
      print "--------"
      if(fr.cube1[5][2][1] == fr.cube1[3][1][1]):
         topToLeftRed()
      elif(fr.cube1[5][2][1] == fr.cube1[1][1][1]):
         topToRightRed()
      return
    
    if(fr.cube1[3][1][1] == fr.cube1[3][0][1] and fr.cube1[5][1][0] != 'y'):
      print "Blue side"
      print "---------"
      if(fr.cube1[5][1][0] == fr.cube1[2][1][1]):
         topToLeftBlue()
      elif(fr.cube1[5][1][0] == fr.cube1[4][1][1]):
         topToRightBlue()
      return
    
    if(fr.cube1[1][1][1] == fr.cube1[1][0][1] and fr.cube1[5][1][2] != 'y'):
      print "Green side"
      print "----------"
      if(fr.cube1[5][1][2] == fr.cube1[4][1][1]):
         topToLeftGreen()
      elif(fr.cube1[5][1][2] == fr.cube1[2][1][1]):
         topToRightGreen()
      return
    
    if(fr.cube1[2][1][1] == fr.cube1[2][2][1] and fr.cube1[5][0][1] != 'y'):
      print "Orange side"
      print "------"
      if(fr.cube1[5][0][1] == fr.cube1[1][1][1]):
         topToLeftOrange()
      elif(fr.cube1[5][0][1] == fr.cube1[3][1][1]):
         topToRightOrange()
      return 
    #pf.printFaces(cube)

def solveSecondLayer(): 
   
   secondLayerCheck = 0
   
   # Check if mid green layer is filled
   if( fr.cube1[1][1][0] == 'g' and fr.cube1[1][1][1] == 'g' and fr.cube1[1][1][2] == 'g' ):
      secondLayerCheck+= 1
   # Check if mid orange layer is filled
   if( fr.cube1[2][1][0] == 'o' and fr.cube1[2][1][1] == 'o' and fr.cube1[2][1][2] == 'o' ):
      secondLayerCheck+= 1
   # Check if mid blue layer is filled
   if( fr.cube1[3][1][0] == 'b' and fr.cube1[3][1][1] == 'b' and fr.cube1[3][1][2] == 'b' ):
      secondLayerCheck+= 1
   # Check if mid red layer is filled   
   if( fr.cube1[4][1][0] == 'r' and fr.cube1[4][1][1] == 'r' and fr.cube1[4][1][2] == 'r' ):
      secondLayerCheck+= 1
   

   #print secondLayerCheck 
   while( secondLayerCheck != 4 ):
       
      secondLayerCheck = 0
      topLayerAlign()
      secondLayerComplete()
      # Check if mid green layer is filled
      if( fr.cube1[1][1][0] == 'g' and fr.cube1[1][1][1] == 'g' and fr.cube1[1][1][2] == 'g' ):
         secondLayerCheck+= 1
      # Check if mid orange layer is filled
      if( fr.cube1[2][1][0] == 'o' and fr.cube1[2][1][1] == 'o' and fr.cube1[2][1][2] == 'o' ):
         secondLayerCheck+= 1
      # Check if mid blue layer is filled
      if( fr.cube1[3][1][0] == 'b' and fr.cube1[3][1][1] == 'b' and fr.cube1[3][1][2] == 'b' ):
         secondLayerCheck+= 1
      # Check if mid red layer is filled   
      if( fr.cube1[4][1][0] == 'r' and fr.cube1[4][1][1] == 'r' and fr.cube1[4][1][2] == 'r' ):
         secondLayerCheck+= 1
      
      #print secondLayerCheck
      #print "\n"
      #pf.printFaces(fr.cube1)
      if( secondLayerCheck == 4 ):
         return

