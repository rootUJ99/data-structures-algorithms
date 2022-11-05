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
        x.left = y
        return x

    def splay(self, root, data):
        if root == None or root.data == data:
            return root 
        
        if root.data > data:
            if root.left == None: return root

            if root.left.data > data:
                # zig zig rotation``
                root.left.left = self.splay(root.left.left, data)
                self.LL_Rotations(root)
            elif root.left.data < data:
                # zig zag rotation
                root.left.right = self.splay(root.left.right, data)
                
                if root.left.data != None:
                    root.left = self.LL_Rotations(root.left)
            return root if root.left == None else self.RR_Rotations(root)

        else:
            if root.right == None: return root
            if root.right.data > data:
                # zag zag rotation``
                root.right.right = self.splay(root.right.right, data)
                self.RR_Rotations(root)
            elif root.right.data < data:
                # zag zig roatation
                root.right.left = self.splay(root.right.left, data)

                if root.right.data != None:
                    root.right = self.RR_Rotations(root.right)
            return root if root.right == None else self.LL_Rotations(root)

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
    print(root = s.bst_search(root, 6))
    s.pre_order(root)
