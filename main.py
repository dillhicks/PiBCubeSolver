import cv2
import movement as mv
import scan 
import kociemba 
import orientation as ori
import linkedList


cube = []

def get_Orientation(face):
    if face[1][1] == 'W':
        cube[0] = face;
    else if face[1][1] == 'G':
        cube[1] = face;
    else if face[1][1] == 'O':
        cube[2] = face;
    else if face[1][1] == 'B':
        cube[3] = face;
    else if face[1][1] == 'R':
        cube[4] = face;
    else if face[1][1] == 'Y':
        cube[5] = face;

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

if __name__ == "__main__":
    f1, f2 = scan.init_scan()
    mv.init_turn()
    f3, f4 = scan.init_scan()
    mv.init_turn()
    f5, f6 = scan.init_scan()
    mv.init_turn()
    get_Orientation(f1)
    get_Orientation(f2)
    get_Orientation(f3)
    get_Orientation(f4)
    get_Orientation(f5)
    get_Orientation(f6)

    placement = arrayToKociemba(cube)
    moves = kociemba.solve(placement)
    translateMoves = ori.translateTurns(moves)
    iterator = linkedList.iterator(instrs)
    stringI = ""
    while 1:
        turn = iterator.getTurn()
        stringI += turn + " "
        if not iterator.next():
            break
    print(stringI)





