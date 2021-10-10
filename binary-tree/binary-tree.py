class Node:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree: 
    def __init__(self, root=None):
        self.root = root

    def add_node(self, data):
        if self.root == None:
            self.root =Node(data)
            return

        if data > self.root.data:
            r = self.root
            while r.right:
                r = r.right
            r.right= Node(data)

        if data < self.root.data:
            l = self.root
            while l.left:
                l = l.left
            l.left = Node(data)

    
    def inorder_trav(self, node = None):
        if node == None:
            node = self.root
        if node.left:
            self.inorder_trav(node.left)
        print(node.data)
        if node.right:
            self.inorder_trav(node.right)
    
    def preorder_trav(self, node=None):
        if node == None:
            node = self.root
        print(node.data)
        if node.left:
            self.preorder_trav(node.left)
        if node.right:
            self.preorder_trav(node.right)

    def postorder_trav(self, node=None):
        if node == None:
            node = self.root
        if node.left:
            self.postorder_trav(node.left)
        if node.right:
            self.postorder_trav(node.right)
        print(node.data)


    # def depth(self, node=None):
    #     if node == None:
    #         node = self.root
    #         lDepth = 0
    #         rDepth = 0
        
    #      if data > self.root.data:
    #         r = self.root
    #         while r.right:
    #             r = r.right
    #         r.right= Node(data)

    #     if data < self.root.data:
    #         l = self.root
    #         while l.left:
    #             l = l.left
    #         l.left = Node(data)
        

bt = BTree()
bt.add_node(1)
bt.add_node(2)
bt.add_node(3)
bt.add_node(4)
bt.add_node(5)

bt.inorder_trav()
print('----')
bt.preorder_trav()
print('----')
bt.postorder_trav()
print('----')
# bt.depth()


