
class Node:
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next 

class CircluarQueue:
    def __init__(self):
        self.rear = None
        self.front = None

    def is_empty(self):
        if self.rear == None and self.front == None:
            return True
        return False

    def enqueue(self, data):
        node = Node(data= data)
        if self.is_empty():
            self.rear = node
            self.front = node
            self.rear.next = self.front
            return
        node.next = self.front
        self.rear.next = node
        self.rear = node
    

    def dequeue(self):
        if self.is_empty():
            raise Exception("you can dequeue an empty queue")
            return
        data  = self.front.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
            return data
        self.front = self.front.next
        self.rear.next = self.front
        return data

    def pprint(self):
        if self.is_empty():
            print("None")
            return
        node = self.front
        print(node)
        pointer = node
        while(node):
            print(node.data)
            node = node.next
            if node == self.front:
                break

        

if __name__ == "__main__":
    cq = CircluarQueue()
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.pprint()
    
