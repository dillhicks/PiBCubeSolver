import kociemba
import orientation
import numpy as np
import linkedList
# Array is an array of 2D arrays assosciated with each face
#up,right,front,down,left,back

def translateK(color):
    if color == "r":
        return "F"
    if color == "y":
        return "U"
    if color == "b":
        return "L"
    if color == "g":
        return "R"
    if color == "o":
        return "B"
    if color == "w":
        return "D"
def arrayToKociemba(array):
    string = ""
    i = 0
    face = None
    while i < 6:
        if i == 0:
            #up
            face = array[0]
        elif i == 1:
            #right
            face = array[3]
        elif i == 2:
            #front
            face = array[1]
        elif i == 3:
            #down
            face = array[5]
        elif i == 4:
            #left
            face = array[2]
        else:
            face = array[4]
        row = 0
        col = 0
        num = 0
        while num < 9:
            if col == 3:
                row += 1
                col = 0
            string += translateK(face[row][col])
            num += 1
            col += 1
    return string
            
            
string = kociemba.solve( "FFFLUUBBLFRRURDULLDDDUFLBFLRRFDDBBBBRDRRLFLFUULDRBBDUU" )
print()
print("The Instructions on a Fixed Orientation:")
print(string)
print()
instrs = orientation.translateTurns(string)
iterator = linkedList.iterator(instrs)
stringI = ""
while 1:
    turn = iterator.getTurn()
    stringI += turn + " "
    if not iterator.next():
        break
print("The Instructions Accounting for Changing Orientation:")
print(stringI)
