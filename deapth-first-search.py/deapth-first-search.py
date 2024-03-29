class DFS:
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

    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(vertex)
        print(vertex)
        for node in self.graph_dict[vertex]:
            if node not in visited:
                self.dfs(node, visited)

        

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

g = DFS(graph_adj)
g.dfs(0)


