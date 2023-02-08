class Node:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree: 
    
    '''
    here __add_node and similar methods are declared as private methods 
    
    which are taking an extra argument as root node which is a instance variable

    if not done in this way we need to pass the root as normal parameter
    
    explicitly while calling them after instace creation from the method
    '''
    def __init__(self, root=None):
        self.root = root

    def __add_node(self, root, data):
        if root == None:
            root =Node(data)
            return root

        if data >= root.data:
            root.right = self.__add_node(root.right, data)

        else:
            root.left = self.__add_node(root.left, data)

        return root

    def add_node(self, data):
        self.root = self.__add_node(self.root, data)

    def __inorder_trav(self, node=None):
        if node != None:
            self.__inorder_trav(node.left)
            print(node.data, " ")
            self.__inorder_trav(node.right)

    def inorder_trav(self):
        self.__inorder_trav(self.root)
    
    def __preorder_trav(self, node=None):
        if node != None:
            print(node.data, " ")
            self.__preorder_trav(node.left)
            self.__preorder_trav(node.right)

    def preorder_trav(self):
        self.__preorder_trav(self.root)

    def __postorder_trav(self, node=None):
        if node != None:
            self.__postorder_trav(node.left)
            self.__postorder_trav(node.right)
            print(node.data, " ")

    def postorder_trav(self):
        self.__postorder_trav(self.root)


    def __search_node(self, root, data):
        if root == None: return False
        if data == root.data: return True
        if data <= root.data: 
            return self.__search_node(root.left, data)
        else:
            return self.__search_node(root.right, data)

    def search_node(self, data):
        return self.__search_node(self.root, data)


    

bt = BinarySearchTree()
root = None
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
node_found = bt.search_node(3)
print(node_found)


# root = bt.add_node(root, 1)
# root = bt.add_node(root, 2)
# root = bt.add_node(root, 3)
# root = bt.add_node(root, 4)
# root = bt.add_node(root, 5)

# bt.inorder_trav(root)
# print('----')
# bt.preorder_trav(root)
# print('----')
# bt.postorder_trav(root)
# print('----')
# node_found = bt.search_node(root, 0)
# print(node_found)
