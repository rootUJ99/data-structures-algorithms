class HashMap:
    def __init__(self, size):
        self.input = [None] * size
        self.size = size
        # print(self.input)

    def hash_func(self, key):
        return key % self.size

    def set_key(self, key):
        hash = self.hash_func(key)
        if hash < len(self.input):
            while self.input[hash] != None:
                hash = self.hash_func(hash + 1)
            self.input[hash] = key

    def get_key(self, key):
        hash = self.hash_func(key)
        while self.input[hash] != key and hash < self.size and self.input[hash] != None:
            hash  = self.hash_func(hash + 1)
            if self.input[hash] == key:
                return self.input[hash], hash

    def del_key(self, key):
        hash = self.hash_func(key)
        while self.input[hash] != key and hash < self.size and self.input[hash] != None:
            hash  = self.hash_func(hash + 1)
            if self.input[hash] == key:
                self.input[hash] = None

        


    

h = HashMap(100)
h.set_key(22)
h.set_key(222)
print(h.get_key(222))
h.del_key(222)
print(h.get_key(222))
