class Node:
    def __init__(self, data=0, height=0, left=None, right=None):
        self.data = data
        self.height= height
        self.left= left
        self.right= right


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self,node):
        if node == None:
            return -1
        return node.height

    def calc_balance_factor(self,node):
        if node == None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)  
        
    def pre_order(self, node):
        if node != None:
            print(node.data , " ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def insert(self, data=None, node=None):
        if not node:
            return Node(data)
            # return node
        elif data < node.data:
            node.left = self.insert(data,node.left)
        elif data > node.data:
            node.right = self.insert(data,node.right)
        # else:
        #     return node

        node.height = max(self.get_height(node.left),self.get_height(node.right)) + 1

        b = self.calc_balance_factor(node)

        if b > 1:
            if self.calc_balance_factor(node.left) == 1:
                node = self.LL_rotation(node)
            else:
                node.right = self.RR_rotation(node.left)
                node = self.LL_rotation(node)


        elif b < -1:
            if self.calc_balance_factor(node.right) == -1:
                node = self.RR_rotation(node)
            else:
                node.left = self.LL_rotation(node.right)
                node = self.RR_rotation(node)
        
        return node


    def LL_rotation(self, node):
        child = node.left
        node.left = child.right
        child.right = node
        node.height = max(self.get_height(node.left),self.get_height(node.right)) + 1 
        child.height = max(self.get_height(child.left),self.get_height(child.right)) + 1 
        return child


    def RR_rotation(self, node):
        child = node.right
        node.right = child.left
        child.left = node
        node.height = max(self.get_height(node.left),self.get_height(node.right)) + 1 
        child.height = max(self.get_height(child.left),self.get_height(child.right)) + 1 
        return child


if __name__ == '__main__':

    tree = AVLTree()
    root = None
    root = tree.insert(10, root)
    root = tree.insert(20, root)
    root = tree.insert(30, root)
    tree.pre_order(root)
    print(root.data)