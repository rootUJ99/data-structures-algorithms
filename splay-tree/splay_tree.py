class Node:
    def __init__(self, data=0, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right 


class SplayTree:
    def RR_Rotations(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y


    def LL_Rotations(self, y):
        x = y.right
        y.right = x.left
        x.left = x
        return x

    def splay(self, x):
        pass

    def bst_search(self,root, key):
        return self.splay(root, key)

    def pre_order(self, node):
        if node:
            print(node.data, " ")
            self.pre_order(node.left)
            self.pre_order(node.right)
    
    def insert(self, node, x):
        if not node:
            return Node(x)
        elif x < node.data:
            node.left = self.insert(node.left, x) 
        else:
            node.right = self.insert(node.right, x)
        return node



if __name__ == '__main__':
    s = SplayTree()
    root = None
    root = s.insert(root, 1)
    root = s.insert(root, 2)
    root = s.insert(root, 3)
    root = s.insert(root, 4)
    root = s.insert(root, 6)
    s.pre_order(root)
