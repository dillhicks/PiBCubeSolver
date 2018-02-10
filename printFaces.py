import numpy as np
import string

row = 3
col = 3

def printFace( array ):
   print ""
   for i in range(row):
      for j in range(col):
         if( i == 1 & j == 1):
            string = array[i][j]
            print string.upper(),
         else:
            print array[i][j],
         if( j == col-1 ):
            print ""

def printFaces(array):
   for i in range(row):
      for h in range(3):
         for j in range(col):     
            if( i == 1 & j == 1 ):
               string = array[h][i][j]
               print string.upper(),
            else:
               print array[h][i][j],
      
         print "",   
      print""      

   print ""
   for i in range(row):
      for h in range(3,6):
         for j in range(col):     
            if( i == 1 & j == 1 ):
               string = array[h][i][j]
               print string.upper(),
            else:
               print array[h][i][j],
      
         print "",   
      print""      


w = 'w'
b = 'b'
r = 'r'
o = 'o'
y = 'y'
g = 'g'



white = np.array( [[w,w,w], [w,w,w], [w,w,w]] )
blue = np.array( [[b,b,b], [b,b,b], [b,b,b]] )
red = np.array( [[r,r,r], [r,r,r], [r,r,r]] )
orange = np.array( [[o,o,o], [o,o,o], [o,o,o]] )
yellow = np.array( [[y,y,y], [y,y,y], [y,y,y]] )
green = np.array( [[g,g,g], [g,g,g], [g,g,g]] )

array = [white,blue,red,orange,yellow,green]
printFaces(array)

#printFace(white)
#printFace(blue)
#printFace(red)
#printFace(orange)
#printFace(yellow)
#printFace(green)
