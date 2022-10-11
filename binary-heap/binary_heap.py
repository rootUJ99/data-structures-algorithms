from heapq import heapify


class MaxHeap:
    def __init__(self, n) -> None:
        self.tree_arr = []

    def heapify(self,arr, n, i):
        
        l = 2*i + 1
        r = 2*i + 2
        large = i

        if l < n and arr[l] > arr[large]:
            large = l

        if r < n and arr[r] > arr[large]:
            large = r

        if i!=large:
            arr[i], arr[large] =arr[large], arr[i] 
            self.heapify(arr, n, large)
        
    def insert(self, ele):
        size = len(self.tree_arr)
        if bool(size):
            self.tree_arr.append(ele)
            for i in range(size//2-1, -1, -1):
                self.heapify(self.tree_arr, size, i) 
        else:
            self.tree_arr.append(ele)


    def delete(self, ele):
        size = len(self.tree_arr)

        i = 0
        for i in range(0,size-1):
            if ele == self.tree_arr[i]:
                # self.tree_arr[i] = 0
                break
    
        self.tree_arr[i], self.tree_arr[size-1] = self.tree_arr[size-1], self.tree_arr[i]   

        self.tree_arr.remove(ele)
        
        for i in range(size//2-1, -1, -1):
            self.heapify(self.tree_arr, len(self.tree_arr), i) 


h = MaxHeap(5)
h.insert(1)
h.insert(2)
h.insert(3)
h.insert(4)
h.insert(5)
h.insert(6)
print(h.tree_arr)



