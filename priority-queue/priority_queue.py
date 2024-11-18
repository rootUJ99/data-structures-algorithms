class PriorityQueue:
    def __init__(self):
        self.heap = []

    def heapify(self, n, i):
        parent = i 
        left = i * 2 + 1
        right = i * 2 + 2

        if left < n and self.heap[left][0] < self.heap[parent][0]:
            parent = left

        if right < n and self.heap[right][0] < self.heap[parent][0]:
            parent = right

        if i!= parent:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i] 
            self.heapify(n, parent)

    def push(self, node):
        self.heap.append(node)
        l = len(self.heap)
        for i in range(l // 2 - 1, -1, -1):
            self.heapify(l, i)


    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]


    def pop(self):
        if len(self.heap) == 0:
            return None
        
        item = self.heap[0]

        if len(self.heap) == 1:
            parent = self.heap.pop(0)
            return parent
        
        self.heap[0] = self.heap.pop()

        self.heapify(len(self.heap), 0)

        return item

if __name__ == "__main__":
    pq = PriorityQueue()
    tasks = [
        (1, "do this"),
        (5, "do that"),
        (3, "do that that"),
        (4, "do this that"),
    ]
    for i in tasks:
        pq.push(i)
    print(pq.heap)
    pq.pop()
    print(pq.peek())
    print(pq.heap)
