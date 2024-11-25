class UnionFind():

    def __init__(self, size):
        self.size = size
        self.rank = [0] * size 
        self.parent = list(range(size))
        print(self.parent)

    def union(self, x, y):
        f_x = self.find(x) 
        f_y = self.find(y)
        if f_x == f_y:
            return
        
        if self.rank[f_x] < self.rank[f_y]:
            self.parent[f_x] = f_y
        elif self.rank[f_y] < self.rank[f_x]:
            self.parent[f_y] = f_x
        else:
            self.parent[f_y] = f_x
            self.rank[f_x] += 1
        self.size =-1 

    def find(self, x):
        # print(x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    

if __name__ == "__main__":
    
    unions = [(1,5), (3,2), (2,1), (4,7), (6,7), (8,9)]

    u = UnionFind(10)
    for i in unions:
        x, y = i
        u.union(x, y)

    print(u.parent, u.rank)
    is_conn_list = [(3,5), (6,8), (1,2)] 
    for i in is_conn_list:
        x, y = i
        is_conn = u.is_connected(x,y)
        print(is_conn)
