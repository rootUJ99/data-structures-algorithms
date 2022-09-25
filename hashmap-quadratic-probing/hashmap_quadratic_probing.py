class HashMap:
    def __init__(self, size):
        self.input = [None] * size
        self.size = size
        # print(self.input)

    def hash_func(self, key):
        return key % self.size

    def set_key(self, key):
        hash = self.hash_func(key)
        i = 0
        indx = 0
        while i < self.size and self.input[indx] != None:
            indx = self.hash_func(hash + i * i)
            i+=1
        self.input[indx] = key

    def get_key(self, key):
        hash = self.hash_func(key)
        i = 0 
        indx = 0
        while i < self.size:
            indx = self.hash_func(hash + i * i)
            if self.input[indx] == key:
                return self.input[indx], indx
            i+=1

    def del_key(self, key):
        hash = self.hash_func(key)
        i = 0
        indx = 0
        while self.input[indx] != key and i < self.size:
            indx  = self.hash_func(hash + i * i)
            if self.input[indx] == key:
                self.input[indx] = None
            i+=1
        


    

h = HashMap(100)
h.set_key(22)
h.set_key(222)
print(h.get_key(22))
h.del_key(222)
print(h.get_key(222))

