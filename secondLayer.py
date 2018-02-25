import numpy as np
#from printFaces import printFaces
#import faceRotation as fr
#import faceRotation as fr
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
   





