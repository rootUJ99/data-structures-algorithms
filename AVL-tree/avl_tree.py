from itertools import tee


class Node:
    def __init__(self, data=0, height=0, left=None, right=None):
        self.data = data
        self.height= height
        self.left= left
        self.right= right


class AVLTree:
    def __init__(self, root=None):
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
        node.height = max(self.get_height(node.left),self.get_height(node.right)) 

    def insert(self, data=None, node=None):
        if node:
            node = self.root
        if self.root == None:
            self.root = Node()
            return self.root
        elif data < self.root.data:
            self.root.left = self.insert(data,self.root.left)
        elif data > self.root.data:
            self.root.right = self.insert(data,self.root.right)
        else:
            return self.root

        self.root.height = max(self.get_height(self.root.left),self.get_height(self.root.rightS)) 

        b = self.calc_balance_factor(self.root)

        if b < 1:
            if self.calc_balance_factor(self.root.left == 1):
                self.root = self.LL_rotation(self.root)
            else:
                self.root.right = self.RR_rotation(self.root.right)
                self.root = self.LL_rotation(self.root)


        elif b < -1:
            if self.calc_balance_factor(self.root.left == 1):
                self.root = self.RR_rotation(self.root)
            else:
                self.root.left = self.LL_rotation(self.root.left)
                self.root = self.RR_rotation(self.root)


    def LL_rotation(self, node):
        child = node.left
        node.left = child.right
        child.right = node
        node.height = max(self.get_height(node.left),self.get_height(node.right)) + 1 
        child.height = max(self.get_height(child.left),self.get_height(child.right)) + 1 
        return node


    def RR_rotation(self, node):
        child = node.right
        node.right = child.left
        child.left = node
        node.height = max(self.get_height(node.left),self.get_height(node.right)) + 1 
        child.height = max(self.get_height(child.left),self.get_height(child.right)) + 1 
        return node


if __name__ == '__main__':

    tree = AVLTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.pre_order()