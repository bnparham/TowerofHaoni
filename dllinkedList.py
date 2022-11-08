class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None
        self.Previous = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
        else:
            cur = self.head
            while(cur.Next):
                cur = cur.Next
            cur.Next = newNode
            newNode.Previous = cur
            
    def print_list(self):
        cur = self.head
        while(cur):
            print(cur.data)
            cur = cur.Next