class CircularQueue:
    def __init__(self, N):
        self.N = N
        self.queue = [None] * N
        self.head = -1
        self.tail = -1

    def enqueue(self, data):
        if (self.tail + 1) % self.N == self.head:
            print('queue is full')
        elif self.tail == -1:
            self.head = self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.N
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            print('queue is empty')
        elif self.head == self.tail:
            temp = self.queue[self.head]
            # self.queue[self.head] = None
            self.head = self.tail = -1 
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.N
            # self.queue[self.head] = None
            return temp
    
    def print(self):
        print(self.queue)    

    def cqprint(self):
        if self.head == -1:
            print("no element in queue")
        elif self.tail >= self.head:
            for i in range(self.head, self.tail+1):
                print(self.queue[i])
            print()
        else:
            for i in range(self.head, self.K):
                print(self.queue[i], end="")
            for i in range(0, self.tail +1):
                print(self.queue[i], end="")
            print()
cq = CircularQueue(4)
cq.enqueue(1)
cq.enqueue(5)
cq.enqueue(7)
cq.enqueue(3)
cq.dequeue()
cq.dequeue()
cq.cqprint()
print(cq.head, cq.tail)


