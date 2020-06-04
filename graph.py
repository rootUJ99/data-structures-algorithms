class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [None] * vertex

    def add_node(self, src, dest):
        sourceNode = Node(src)
        destNode = Node(dest)
        sourceNode.next = self.graph[dest]
        destNode.next = self.graph[src]
        self.graph[src] = sourceNode
        self.graph[dest] = destNode

    def print(self):
        for i in range(self.vertex):
            temp = self.graph[i]
            llist = ''
            while temp:
                llist = f"{llist} {str(temp.data)} {'-->' if temp.next != None else ''}"
                temp = temp.next
            print(llist)


g = Graph(5)

g.add_node(0,1)
g.add_node(0,4)
g.add_node(1,2)
g.add_node(1,3)
g.add_node(2,3)
g.add_node(3,4)

g.print()