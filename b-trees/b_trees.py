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
    
    def search(self, x, key):
        indx = 0
        if x == None: 
            return x
        
        for i in range(x.n):
            indx = i
            if key < x.key[i]:
                break
            if key == x.key[i]:
                return x
        
        if x.leaf:
            return None
        else:
            return self.search(x.child[i], key)

    def split(self, x, pos, y):
        pass

b = BNode()
