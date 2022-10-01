class Node:
    def __init__(self, data=0, height=0, left=None, right=None):
        self.data = data
        self.height= height
        self.left= left
        self.right= right


class AVLTree:
    def __init__(self, root):
        self.root= root 

    def get_height(self,node):
        if node == None:
            return -1
        return node.height

    def calc_balance_factor(self,node):
        if node == None:
            return None
        return self.get_height(node.left) - self.get_height(node.right)  
        
    def pre_order(self, node):
        if node != None:
            print(node.data)
            self.pre_order(node.left)
            self.pre_order(node.right)

