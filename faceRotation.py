import numpy as np
from printFaces import printFaces
w = 'w'
b = 'b'
r = 'r'
o = 'o'
y = 'y'
g = 'g'

global bottom
global left
global front
global back
global top
global right
global cube1


bottom = np.array( [[w,w,w],[w,w,w],[w,w,w]] )
left = np.array( [[y,r,r],[y,b,b],[b,b,b]] )
front = np.array( [[y,g,g],[y,r,b],[r,r,r]] )
back = np.array( [[o,o,o],[g,o,b],[o,y,b]] )
top = np.array( [[g,r,y],[g,y,o],[b,o,r]] )
right = np.array( [[y,y,o],[o,g,r],[g,g,g]] )

cube1 = np.array( [bottom,right,back,left,front,top] )

def rotateClockwise( data ):
   print "rotating clockwise"
   first = np.array( data[0,0] )
   second = np.array( data[1,0] )
   third = np.array( data[2,0] )
   fourth = np.array( data[2,1] )
   fifth = np.array( data[2,2] )
   sixth = np.array( data[1,2] )
   seventh = np.array( data[0,2] )
   eighth = np.array( data[0,1] )
   
   data[0,0] = third
   data[1,0] = fourth
   data[2,0] = fifth
   data[2,1] = sixth
   data[2,2] = seventh
   data[1,2] = eighth
   data[0,2] = first
   data[0,1] = second

   

def rotateCounter( data ):
   print "rotating counter-clockwise"
   first = np.array( data[0,0] )
   second = np.array( data[1,0] )
   third = np.array( data[2,0] )
   fourth = np.array( data[2,1] )
   fifth = np.array( data[2,2] )
   sixth = np.array( data[1,2] )
   seventh = np.array( data[0,2] )
   eighth = np.array( data[0,1] )
   
   data[0,0] = seventh 
   data[1,0] = eighth
   data[2,0] = first
   data[2,1] = second
   data[2,2] = third
   data[1,2] = fourth
   data[0,2] = fifth
   data[0,1] = sixth

   
def rotateFront():
   print "rotating front face"
   top1 = np.array( top[2,0] )
   top2 = np.array( top[2,1] )
   top3 = np.array( top[2,2] )

   right1 = np.array( right[0,0] )
   right2 = np.array( right[1,0] )
   right3 = np.array( right[2,0] )

   bottom1 = np.array( bottom[0,0] )
   bottom2 = np.array( bottom[0,1] )
   bottom3 = np.array( bottom[0,2] )

   left1 = np.array( left[0,2] )
   left2 = np.array( left[1,2] )
   left3 = np.array( left[2,2] )

   top[2,0] = left3
   top[2,1] = left2
   top[2,2] = left1

   right[0,0] = top1
   right[1,0] = top2
   right[2,0] = top3
   
   bottom[0,0] = right3
   bottom[0,1] = right2
   bottom[0,2] = right1

   left[0,2] = bottom1
   left[1,2] = bottom2
   left[2,2] = bottom3
   
   rotateClockwise( front )

   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1

def rotateBack():
   print "rotating back face"
   top_face = np.array( top[0,:] )
   right_face = np.array( right[:,2] )
   bottom_face = np.array( bottom[2,:] )
   left_face = np.array( left[:,0] )

   top[0,:] = right_face
   reverse1 = bottom_face[::-1]
   right[:,2] = reverse1
   bottom[2,:] = left_face
   reverse = top_face[::-1]
   left[:,0] = reverse
   

   rotateClockwise( back )

   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1

def rotateRight():
   print "rotating right face"
   front1 = np.array( front[0,2] )
   front2 = np.array( front[1,2] )
   front3 = np.array( front[2,2] )

   top1 = np.array( top[0,2] )
   top2 = np.array( top[1,2] )
   top3 = np.array( top[2,2] )

   back1 = np.array( back[0,2] )
   back2 = np.array( back[1,2] )
   back3 = np.array( back[2,2] )

   bottom1 = np.array( bottom[0,2] )
   bottom2 = np.array( bottom[1,2] )
   bottom3 = np.array( bottom[2,2] )

   front[0,2] = bottom1
   front[1,2] = bottom2
   front[2,2] = bottom3

   top[0,2] = front1
   top[1,2] = front2
   top[2,2] = front3

   back[0,2] = top1
   back[1,2] = top2
   back[2,2] = top3

   bottom[0,2] = back1
   bottom[1,2] = back2
   bottom[2,2] = back3

   rotateClockwise( right )

   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1

def rotateLeft():
   print "rotating left face"
   top1 = np.array( top[0,0] )
   top2 = np.array( top[1,0] )
   top3 = np.array( top[2,0] )

   front1 = np.array( front[0,0] )
   front2 = np.array( front[1,0] )
   front3 = np.array( front[2,0] )

   bottom1 = np.array( bottom[0,0] )
   bottom2 = np.array( bottom[1,0] )
   bottom3 = np.array( bottom[2,0] )

   back1 = np.array( back[0,0] )
   back2 = np.array( back[1,0] )
   back3 = np.array( back[2,0] )

   top[0,0] = back1
   top[1,0] = back2
   top[2,0] = back3

   front[0,0] = top1
   front[1,0] = top2
   front[2,0] = top3

   bottom[0,0] = front1
   bottom[1,0] = front2
   bottom[2,0] = front3

   back[0,0] = bottom1
   back[1,0] = bottom2
   back[2,0] = bottom3

   rotateClockwise( left )

   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1

def rotateTop():
   print "rotating top face"
   front1 = np.array( front[0,0] )
   front2 = np.array( front[0,1] )
   front3 = np.array( front[0,2] )

   right1 = np.array( right[0,0] )
   right2 = np.array( right[0,1] )
   right3 = np.array( right[0,2] )

   back1 = np.array( back[2,0] )
   back2 = np.array( back[2,1] )
   back3 = np.array( back[2,2] )

   left1 = np.array( left[0,0] )
   left2 = np.array( left[0,1] )
   left3 = np.array( left[0,2] )

   front[0,0] = right1
   front[0,1] = right2
   front[0,2] = right3

   right[0,0] = back3
   right[0,1] = back2
   right[0,2] = back1

   back[2,0] = left3
   back[2,1] = left2
   back[2,2] = left1

   left[0,0] = front1
   left[0,1] = front2
   left[0,2] = front3

   rotateClockwise( top )
   
   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1

def rotateBottom():
   print "rotating bottom face"
   front_face = np.array( front[2,:] )
   right_face = np.array( right[2,:] )
   back_face = np.array( back[0,:] )
   left_face = np.array( left[2,:] )

   front[2,:] = left_face
   right[2,:] = front_face
   back[0,:] = right_face
   left[2,:] = back_face      
   
   rotateClockwise( bottom )

   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1

def rotateCCFront():
   print "rotating front face" 
   top1 = np.array( top[2,0] )
   top2 = np.array( top[2,1] )
   top3 = np.array( top[2,2] )
   
   right1 = np.array( right[0,0] )
   right2 = np.array( right[1,0] )
   right3 = np.array( right[2,0] )
   
   bottom1 = np.array( bottom[0,0] )
   bottom2 = np.array( bottom[0,1] )
   bottom3 = np.array( bottom[0,2] )
   
   left1 = np.array( left[0,2] )
   left2 = np.array( left[1,2] )
   left3 = np.array( left[2,2] )
   
   top[2,0] = right1
   top[2,1] = right2
   top[2,2] = right3
   
   right[0,0] = bottom3
   right[1,0] = bottom2
   right[2,0] = bottom1
   
   bottom[0,0] = left1
   bottom[0,1] = left2
   bottom[0,2] = left3
   
   left[0,2] = top3
   left[1,2] = top2
   left[2,2] = top1
   
   rotateCounter( front )

   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1

def rotateCCBack():
   print "rotating back face"
   top_face = np.array( top[0,:] )
   right_face = np.array( right[:,2] )
   bottom_face = np.array( bottom[2,:] )
   left_face = np.array( left[:,0] )

   reverse = left_face[::-1]
   top[0,:] = reverse 
   right[:,2] = top_face
   reverse1 = right_face[::-1]
   bottom[2,:] = reverse1
   left[:,0] = bottom_face

   rotateCounter( back )

   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1

def rotateCCRight():
   print "rotating right face"
   front1 = np.array( front[0,2] )
   front2 = np.array( front[1,2] )
   front3 = np.array( front[2,2] )

   top1 = np.array( top[0,2] )
   top2 = np.array( top[1,2] )
   top3 = np.array( top[2,2] )

   back1 = np.array( back[0,2] )
   back2 = np.array( back[1,2] )
   back3 = np.array( back[2,2] )

   bottom1 = np.array( bottom[0,2] )
   bottom2 = np.array( bottom[1,2] )
   bottom3 = np.array( bottom[2,2] )

   front[0,2] = top1
   front[1,2] = top2
   front[2,2] = top3

   top[0,2] = back1
   top[1,2] = back2
   top[2,2] = back3

   back[0,2] = bottom1
   back[1,2] = bottom2
   back[2,2] = bottom3

   bottom[0,2] = front1
   bottom[1,2] = front2
   bottom[2,2] = front3

   rotateCounter( right )

   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1

def rotateCCLeft():
   print "rotating left face"
   top1 = np.array( top[0,0] )
   top2 = np.array( top[1,0] )
   top3 = np.array( top[2,0] )

   front1 = np.array( front[0,0] )
   front2 = np.array( front[1,0] )
   front3 = np.array( front[2,0] )

   bottom1 = np.array( bottom[0,0] )
   bottom2 = np.array( bottom[1,0] )
   bottom3 = np.array( bottom[2,0] )

   back1 = np.array( back[0,0] )
   back2 = np.array( back[1,0] )
   back3 = np.array( back[2,0] )

   top[0,0] = front1
   top[1,0] = front2
   top[2,0] = front3

   front[0,0] = bottom1
   front[1,0] = bottom2
   front[2,0] = bottom3

   bottom[0,0] = back1
   bottom[1,0] = back2
   bottom[2,0] = back3

   back[0,0] = top1
   back[1,0] = top2
   back[2,0] = top3

   rotateCounter( left )

   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1

def rotateCCTop():
   print "rotating top face"
   front1 = np.array( front[0,0] )
   front2 = np.array( front[0,1] )
   front3 = np.array( front[0,2] )

   right1 = np.array( right[0,0] )
   right2 = np.array( right[0,1] )
   right3 = np.array( right[0,2] )

   back1 = np.array( back[2,0] )
   back2 = np.array( back[2,1] )
   back3 = np.array( back[2,2] )

   left1 = np.array( left[0,0] )
   left2 = np.array( left[0,1] )
   left3 = np.array( left[0,2] )

   front[0,0] = left1
   front[0,1] = left2
   front[0,2] = left3

   right[0,0] = front1
   right[0,1] = front2
   right[0,2] = front3

   back[2,0] = right3
   back[2,1] = right2
   back[2,2] = right1

   left[0,0] = back3
   left[0,1] = back2
   left[0,2] = back1

   rotateCounter( top )
   
   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1

def rotateCCBottom():
   print "rotating bottom face"
   front_face = np.array( front[2,:] )
   right_face = np.array( right[2,:] )
   back_face = np.array( back[0,:] )
   left_face = np.array( left[2,:] )

   front[2,:] = right_face
   right[2,:] = back_face
   back[0,:] = left_face
   left[2,:] = front_face     
   
   rotateCounter( bottom )

   tmpCube = np.array( [bottom,right,back,left,front,top] )
   cube1 = tmpCube
   return cube1



#tmp = np.array( [bottom,right,back,left,front,top] )
#cube1 = tmp


#rotateTop();
#print front
#print back
#print top 
#print bottom
#print left
#print right


#printFaces(cube1);



#printFaces(cube1);
#rotateCCBottom()
#rotateTop()
#rotateLeft()
#rotateCCRight()
#rotateBottom()
#rotateCCTop()
#rotateLeft()
#rotateRight()



#print "front face = "
#print front
#print "back face = "
#print back
#print "left face = "
#print left
#print "right face = "
#print right
#print "top face = "
#print top
#print "bottom = "
#print bottom
