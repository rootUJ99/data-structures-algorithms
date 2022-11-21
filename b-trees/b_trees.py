class BNode:
    def __init__(self, leaf=False) -> None:
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, T) -> None:
        self.root = BNode()
        self.T = T

    def insert(self, key):
        pass

    def insert_non_full(self, x, key):
        pass

    def split_child(self, x, i):
        pass

    def print_tree(self, x, l=0):
        print("level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end="")
        print()

        l+=1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

    def search_key(self, key, x=None):
        if x is not None: 
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i+=1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                self.search_key(key, x.child[i])
        else:
            self.search_key(key, self.root)

if __name__ == "__main__":
    b = BTree()
