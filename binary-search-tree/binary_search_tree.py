class Node:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree: 
    def __init__(self, root=None):
        self.root = root

    def add_node(self, root, data):
        if root == None:
            root =Node(data)
            return root

        if data >= root.data:
            root.right = self.add_node(root.right, data)

        else:
            root.left = self.add_node(root.left, data)

        return root

    
    def inorder_trav(self, node=None):
        if node != None:
            self.inorder_trav(node.left)
            print(node.data, " ")
            self.inorder_trav(node.right)
    
    def preorder_trav(self, node=None):
        if node != None:
            print(node.data, " ")
            self.inorder_trav(node.left)
            self.inorder_trav(node.right)

    def postorder_trav(self, node=None):
        if node != None:
            self.inorder_trav(node.left)
            self.inorder_trav(node.right)
            print(node.data, " ")


    def search_node(self, root, data):
        if root == None: return False
        if data == root.data: return True
        if data <= root.data: 
            return self.search_node(root.left, data)
        else:
            return self.search_node(root.right, data)
        

bt = BTree()
root = None
root = bt.add_node(root, 1)
root = bt.add_node(root, 2)
root = bt.add_node(root, 3)
root = bt.add_node(root, 4)
root = bt.add_node(root, 5)

bt.inorder_trav(root)
print('----')
bt.preorder_trav(root)
print('----')
bt.postorder_trav(root)
print('----')
node_found = bt.search_node(root, 0)
print(node_found)


