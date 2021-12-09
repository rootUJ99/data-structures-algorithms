from collections import deque

class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.graph_dict = None
        if type(graph) == list:
            self.graph_dict = self.convert_to_dict(graph)
    
    def convert_to_dict(self, graph: list):
        map = {}
        for i in range(len(graph) * len(graph[0])):
            row = i // len(graph[0])
            col = i % len(graph[0])
            if graph[row][col] == 1:
                try:
                    map[row].append(col)
                except:
                    map[row] = [col]
        print(map, 'map')
        return map

    def bfs(self, vertex):
        queque, visited = deque([vertex]), set([vertex])
        while queque:
            vertex = queque.popleft()
            print(vertex)
            for node in self.graph_dict[vertex]:
                if node not in visited:
                    queque.append(node)
                    visited.add(node)


        

graph_dict = {
    0: [1,3],
    1: [0,2],
    2: [1,3],
    3: [2,0]
}

graph_adj = [
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0],
]

g = BFS(graph_adj)
g.bfs(0)

