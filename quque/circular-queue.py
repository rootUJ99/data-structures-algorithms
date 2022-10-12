class CircularQueue:
    def __init__(self, N):
        self.N = N
        self.queue = [None] * N
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.N == self.front:
            print('queue is full')
        elif self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.N
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print('queue is empty')
        elif self.front == self.rear:
            temp = self.queue[self.front]
            # self.queue[self.front] = None
            self.front = self.rear = -1 
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.N
            # self.queue[self.front] = None
            return temp
    
    def print(self):
        print(self.queue)    

    def cqprint(self):
        if self.front == -1:
            print("no element in queue")
        elif self.rear >= self.front:
            for i in range(self.front, self.rear+1):
                print(self.queue[i])
            print()
        else:
            for i in range(self.front, self.K):
                print(self.queue[i], end="")
            for i in range(0, self.rear +1):
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
print(cq.front, cq.rear)


