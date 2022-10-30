from random import random


class Node():
    def __init__(self, data):
        self.data = data
        self.priority = int(random() * 100)
        self.left = None
        self.right = None
class Treap():
    def __init__(self, root=None):
        self.root = root
    
    def LL_rotation(self, root):
        right = root.right
        node = root.right.left

        # rotation
        right.left = root
        root.right = node

        # set node
        root = right
        return root


    def RR_rotation(self, root):
        left = root.left
        node = root.left.right

        # rotation
        left.right = root
        root.left = node

        # set node
        root = left 
        return root
        
    
    def search_node(self, root, key):
        if root == None:
            return False
            
        if key == root.data: 
            return True

        if root.root < key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)


    def insert_node(self, root=None, data=None):
        if root == None:
            return Node(data)
        
        if data < root.data:
            root.left = self.insert_node(root.left, data)

            if root.left != None and root.left.priority > root.priority:
                root = self.RR_rotation(root)
        else:
            root.right = self.insert_node(root.right, data)

            if root.right != None and root.right.priority > root.priority:
                root = self.LL_rotation(root)

        return root

    def delete_node(self):
        pass
    
    def print_treap(self, node):
        if node != None:
            print(node.data , " ")
            self.print_treap(node.left)
            self.print_treap(node.right)

if __name__ == "__main__":
    t = Treap()
    root = None
    root = t.insert_node(root, 1)
    root = t.insert_node(root, 2)
    root = t.insert_node(root, 3)
    root = t.insert_node(root, 5)
    root = t.insert_node(root, 7)
    t.print_treap(root)