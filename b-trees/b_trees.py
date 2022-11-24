class BNode:
    def __init__(self, leaf=False) -> None:
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, T) -> None:
        self.root = BNode(True)
        self.T = T

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2*self.T) - 1:
            temp = BNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, x, key):
        i = len(x.keys) -1 
        if x.leaf:
            x.keys.append((None, None))
            while i >=0 and key[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -=1
            x.keys[i+1] = key
        else:
            while i >=0 and key[0] < x.keys[i][0]:
                i -=1
            i+=1
            if len(x.child[i].keys) == (2*self.T) -1:
                self.split_child(x,i)
                if key[0] > x.keys[i][0]:
                    i+=1
            self.insert_non_full(x.child[i], key)

    def split_child(self, x, i):
        t = self.T
        y = x.child[i]
        z = BNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t-1])
        z.keys = y.keys[t: (2*t) -1]
        y.keys = y.keys[0: t-1]
        if not y.leaf:
            z.child = y.child[t: 2*t]
            y.child = y.child[0: t-1]

    def print_tree(self, x, l=0):
        print("level ", l, " ", len(x.keys), end=" : ")
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

    def delete(self, x, key):
        pass

    def delete_internal_nodes(seld, x, key, i):
        pass

    def delete_merge(self, x, i, j):
        pass

    def delete_predecessor(self, x):
        pass

    def delete_sucessor(self, x):
        pass

    def delete_sibling(self, x, i, j):
        pass

if __name__ == "__main__":
    b = BTree(5)

    for i in range(20):
        b.insert((i, i*2))
    
    b.print_tree(b.root)
