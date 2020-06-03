class Tree:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree: 
    def __init__(self, root=None):
        self.root = root

    def add_node(self, data):
        if self.root == None:
            self.root = data
            return
        # elif data > 
