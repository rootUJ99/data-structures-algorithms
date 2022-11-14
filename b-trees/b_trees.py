T = 3
class BNode:
    def __init__(self):
        self.n = n 
        self.key = [None] * (2 *T -1)
        self.child = [None] * 2 *T  
        self.isChild = True
    
    def find(self, k):
        for i in range(self.n):
            if self.key[i] == k:
                return i
    
        return -1
    
    def search(self, key):
        pass


b = BNode()
