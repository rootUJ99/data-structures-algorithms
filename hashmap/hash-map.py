class HashMap:
    def __init__(self):
        self.SIZE = 100
        self.arr = [[] for i in range(self.SIZE)]

    def hash_function(self, key):
        index = 0
        for k in key:
            index+=ord(k)
        return index%self.SIZE

    def __setitem__(self, key, value):
        index = self.hash_function(key)
        self.arr[index]=value

    def __getitem__(self, key):
        index = self.hash_function(key)
        return self.arr[index]

    def __delitem__(self, key):
        del(self.arr[self.hash_function(key)])

h = HashMap()
# h.hash_function('something')
h['something']='just Like this'
h['sometihng']='just Like'
print(h['something'])
