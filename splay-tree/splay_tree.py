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

    def pre_order(self, node):
        if node:
            print(node.data, " ")
            self.pre_order(node.left)
            self.pre_order(node.right)
    
    def insert(self, x):
        pass


if __name__ == '__main__':
    s = SplayTree()