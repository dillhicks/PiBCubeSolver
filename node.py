
class Node:
    def __init__(self, turn):
        self.turn = turn
        self.state = None
        self.next = None

    def update(self, state):
        self.state = state
    def append(self, nextNode):
        self.next = nextNode
    def next(self):
        return self.next
