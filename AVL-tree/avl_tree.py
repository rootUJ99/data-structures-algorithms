class Node:
    def __init__(self, data=0, height=0, left=None, right=None):
        self.data = data
        self.height= height
        self.left= left
        self.right= right


class AVLTree:
    def __init__(self):
        self.root= Node()