import numpy as np

y = 'y'
w = 'w'
g = 'g'
b = 'b'
r = 'r'
o = 'o'

top = np.array( [[y,y,y],[y,y,y],[y,y,y]] )
bottom = np.array( [[w,w,w],[w,w,w],[w,w,w]] )
right = np.array( [[g,g,g],[g,g,g],[g,g,g]] )
left = np.array( [[b,b,b],[b,b,b], [b,b,b]] )
front = np.array( [[r,r,r],[r,r,r],[r,r,r]] )
back = np.array( [[o,o,o],[o,o,o],[o,o,o]] )

# Master array
cube = np.array( [bottom,right,back,left,front,top] )

def topLayerAlign( cube ):
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
      return 
   
   print "doesnt work"
   # Check if green side has a T
   if( cube[1][0][1] == 'g' and cube[5][1][0] != 'y' ):
      return
   
   # Check if the orange side has a T
   if( cube[2][2][1] == 'o' and cube[


   if( 

   
   # Check green side
   #if( cube[1][0][1] == 'r' && cube[5][1][2] != 'y' )

   

   
   #if( cube[1][0][1] == cube[1][1][1] && cube[5][1][2] != 'y' ){
   #   if( cube[5][1][2] == 'r' )
   #      topToLeft( cube )
   #   if( cube[5][1][2] == 'o' )
   #      topToRight( cube )
   #}
   #if( cube[2][2][1]
   #
   #if( cube[3][0][1]
   #
   #if( cube[4][0][1]

topLayerAlign(cube)
