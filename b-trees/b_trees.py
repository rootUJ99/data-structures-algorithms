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
        pass

    def search_key(self, key, x=None):
        if x is not None: 
            pass
        else:
            self.search_key(key, self.root)

if __name__ == "__main__":
    b = BTree()
