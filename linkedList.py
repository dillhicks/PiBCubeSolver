import node 

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append(self,newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.tail.append(newNode)
            self.tail = newNode
            self.size += 1
class iterator:
    def __init__(self,List):
        self.curr = List.head
    # Update current Node in iterator if curr.next is not null and return True. 
    def next(self):
        if curr.next is not None:
            self.curr = curr.next
            return True
        else:
            return False
    def getTurn(self):
        return self.curr.turn
    def getState(self):
        return self.curr.state
    def updateTurn(self,newTurn):
        self.curr.turn = newTurn
    def updateState(self,newState):
        self.curr.state = newState

