class Node():
    def __init__(self, data=0, priority=0):
        self.data = data 
        self.priority = priority 
class Treap():
    def __init__():
        pass
    
    def LL_rotation(self, root):
        right = root.right
        node = root.right.left

        # rotation
        right.left = root
        root.right = node

        # set node
        root = right


    def RR_rotation(self, root):
        left = root.left
        node = root.left.right

        # rotation
        left.right = root
        root.left = node

        # set node
        root = left 
        
    
    def search_node(self):
        pass

    def delete_node(self):
        pass
    
    def print_treap(self):
        pass
Treap()