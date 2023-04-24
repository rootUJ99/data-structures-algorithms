from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def add_node(self, vertex, edge):
        self.graph[vertex].add(edge)
        self.graph[edge].add(vertex)


    def breath_first_search(self, vertex):

        visited = set([vertex])
        queue = deque([vertex])        
        while len(queue):
            curr = queue.popleft()
            print(curr)
            for node in self.graph[curr]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)

    
    def depth_first_search(self, vertex):

        visited = set([vertex])
        stack = [vertex]     
        while len(stack):
            curr = stack.pop()
            print(curr)
            for node in self.graph[curr]:
                if node not in visited:
                    stack.append(node)
                    visited.add(node)


    def _depth_first_search_recursive(self, vertext, visited):
        visited.add(vertext)
        print(vertext)
        for node in self.graph[vertext]:
            if node not in visited:
                self._depth_first_search_recursive(node, visited)

    def depth_first_search_recursive(self, vertext):
        
        visited = set()
        self._depth_first_search_recursive(vertext, visited)


graph = Graph()
graph.add_node(1,2)
graph.add_node(1,4)
graph.add_node(2,3)
graph.add_node(3,4)
print(graph.graph)
graph.breath_first_search(1)
print('----')
graph.depth_first_search(1)
print('----')
graph.depth_first_search_recursive(1)