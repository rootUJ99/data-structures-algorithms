class HashMap:
    def __init__(self, size):
        self.input = [None] * size
        self.size = size
        # print(self.input)

    def hash_func1(self, key):
        return key % self.size

    def hash_func2(self, key):
        return (1+key) % (self.size-1)

    def set_key(self, key):
        hash1 = self.hash_func1(key)
        hash2 = self.hash_func2(key)
        i = 0
        indx = 0
        while i < self.size:
            indx = self.hash_func1(hash1 + i* hash2)
            if self.input[indx] == None:
                break
            i+=1
        self.input[indx] = key

    def get_key(self, key):
        hash1 = self.hash_func1(key)
        hash2 = self.hash_func2(key)
        i = 0 
        indx = 0
        while i < self.size:
            indx = self.hash_func1(hash1 + i* hash2)

            if self.input[indx] == key:
                return self.input[indx], indx
            i+=1

    def del_key(self, key):
        hash1 = self.hash_func1(key)
        hash2 = self.hash_func2(key)
        i = 0
        indx = 0
        while self.input[indx] != key and i < self.size:
            indx = self.hash_func1(hash1 + i* hash2)

            if self.input[indx] == key:
                self.input[indx] = None
            i+=1
        


    

h = HashMap(100)
h.set_key(22)
h.set_key(222)
print(h.get_key(22))
h.del_key(222)
print(h.get_key(222))


