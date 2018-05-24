import kociemba
import orientation
import numpy as np
import linkedList
string = kociemba.solve( "FFFLUUBBLFRRURDULLDDDUFLBFLRRFDDBBBBRDRRLFLFUULDRBBDUU" )
#state = np.copy(orientation.orient1)
#newNode = linkedList.Node("L",state)
#linkList = linkedList.linkedList()
#linkList.append(newNode)
#newNode = linkedList.Node("R",state)
#linkList.append(newNode)
#iterator = linkedList.iterator(linkList)

#print(iterator.getTurn())
#print((iterator.getState())[2])
#print(iterator.next())
#print(iterator.getTurn())
#print((iterator.getState())[2])
#state2 = np.copy(state)
#orientation.swapsLeft(state2)
#iterator.updateState(state2)
#print((iterator.getState())[2])
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
