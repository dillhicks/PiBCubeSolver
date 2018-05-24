import numpy as np
import linkedList
import translation as tr
# [0] = top, [1] = front, [2] = left, [3] = right, [4] = back, [5] = bottom
y = "y"
r = "r"
b = "b"
g = "g"
o = "o"
w = "w"
orient1 = np.array([y,r,b,g,o,w])
orient2 = np.array([y,g,r,o,b,w])
orient3 = np.array([y,o,g,b,r,w])
orient4 = np.array([y,b,o,r,g,w])

orient5 = np.array([g,y,o,r,w,b])
orient6 = np.array([g,r,y,w,o,b])
orient7 = np.array([g,w,r,o,y,b])
orient8 = np.array([g,o,w,y,r,b])

orient9 = np.array([w,b,r,o,g,y])
orient10 = np.array([w,o,b,g,r,y])
orient11 = np.array([w,g,o,r,b,y])
orient12 = np.array([w,r,g,b,o,y])

orient13 = np.array([b,y,r,o,w,g])
orient14 = np.array([b,o,y,w,r,g])
orient15 = np.array([b,w,o,r,y,g])
orient16 = np.array([b,r,w,y,o,g])

orient17 = np.array([r,w,b,g,y,o])
orient18 = np.array([r,g,w,y,b,o])
orient19 = np.array([r,y,g,b,w,o])
orient20 = np.array([r,b,y,w,g,o])

orient21 = np.array([o,b,w,y,g,r])
orient22 = np.array([o,y,b,g,w,r])
orient23 = np.array([o,g,y,w,b,r])
orient24 = np.array([o,w,g,b,y,r])

def swapsLeft(orient):
    val0 = orient[0]
    val1 = orient[1]
    val2 = orient[2]
    val3 = orient[3]
    val4 = orient[4]
    val5 = orient[5]
    orient[0] = val3
    orient[1] = val0
    orient[2] = val4
    orient[3] = val1
    orient[4] = val5
    orient[5] = val2
def swapsFront(orient):
    val0 = orient[0]
    val1 = orient[1]
    val2 = orient[2]
    val3 = orient[3]
    val4 = orient[4]
    val5 = orient[5]
    orient[0] = val4
    orient[1] = val0
    orient[2] = val2
    orient[3] = val3
    orient[4] = val5
    orient[5] = val1
def swapsUp(orient):
    val0 = orient[0]
    val1 = orient[1]
    val2 = orient[2]
    val3 = orient[3]
    val4 = orient[4]
    val5 = orient[5]
    orient[0] = val4
    orient[1] = val2
    orient[2] = val5
    orient[3] = val0
    orient[4] = val3
    orient[5] = val1
def swapsBack(orient):
    val0 = orient[0]
    val1 = orient[1]
    val2 = orient[2]
    val3 = orient[3]
    val4 = orient[4]
    val5 = orient[5]
    orient[0] = val1
    orient[1] = val5
    orient[2] = val2
    orient[3] = val3
    orient[4] = val0
    orient[5] = val4

    

def updateOrient(orientation,turn):
    if turn == "L" or turn == "L'":
        swapsLeft(orientation)
    elif turn == "F" or turn == "F'":
        swapsFront(orientation)
    elif turn == "U" or turn == "U'":
        swapsUp(orientation)
    elif turn == "B" or turn == "B'":
        swapsBack(orientation)
def translateMove(instr,orient):
    move = None
    if (orient == orient1).all():
        move = tr.translate1(instr)
    elif (orient == orient2).all():
        move = tr.translate2(instr)
    elif (orient == orient3).all():
        move = tr.translate3(instr)
    elif (orient == orient4).all():
        move = tr.translate4(instr)
    elif (orient == orient5).all():
        move = tr.translate5(instr)
    elif (orient == orient6).all():
        move = tr.translate6(instr)
    elif (orient == orient7).all():
        move = tr.translate7(instr)
    elif (orient == orient8).all():
        move = tr.translate8(instr)
    elif (orient == orient9).all():
        move = tr.translate9(instr)
    elif (orient == orient10).all():
        move = tr.translate10(instr)
    elif (orient == orient11).all():
        move = tr.translate11(instr)
    elif (orient == orient12).all():
        move = tr.translate12(instr)
    elif (orient == orient13).all():
        move = tr.translate13(instr)
    elif (orient == orient14).all():
        move = tr.translate14(instr)
    elif (orient == orient15).all():
        move = tr.translate15(instr)
    elif (orient == orient16).all():
        move = tr.translate16(instr)
    elif (orient == orient17).all():
        move = tr.translate17(instr)
    elif (orient == orient18).all():
        move = tr.translate18(instr)
    elif (orient == orient19).all():
        move = tr.translate19(instr)
    elif (orient == orient20).all():
        move = tr.translate20(instr)
    elif (orient == orient21).all():
        move = tr.translate21(instr)
    elif (orient == orient22).all():
        move = tr.translate22(instr)
    elif (orient == orient23).all():
        move = tr.translate23(instr)
    elif (orient == orient24).all():
        move = tr.translate24(instr)
    return move
def translateTurns(turns):
    size = len(turns)
    linkList = linkedList.linkedList()
    i = 0
    firstState = np.copy(orient1)
    string = "x"
    rotation = None
    while i < size:
        if i+1 < size:
            if turns[i+1:i+2] == "'":
                rotation = turns[i:i+2]
                i += 3
            else:
                rotation = turns[i:i+1]
                i += 2
        else:
            rotation = turns[i:i+1]
            i += 2
        newNode = linkedList.Node(rotation,firstState)
        string += rotation
        linkList.append(newNode)
    iterator = linkedList.iterator(linkList)
    while 1:
        turn = iterator.getTurn()
        #First state may be uninitialized, must figure out
        state = iterator.getState()
        #print(state[0])
        newTurn = translateMove(turn,state)
        iterator.updateTurn(newTurn)
        updateOrient(state,turn)
        if iterator.next():
            iterator.updateState(state)
        else:
            break
    return linkList
