class Graph():
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def get_vertices(self):
        vertices = set([])
        for i in self.graph:
            vertices.add(i)
            for j, _ in self.graph[i]:
                    vertices.add(j)
        return vertices

    def get_distances(self):
        vertices = self.get_vertices()
        distances = {}
        for i in vertices:
            distances[i] = {}
            for j in vertices:
                distances[i][j] = float("inf") 

        return distances

    def floyed_warshell_shortest_path(self):
        distances = self.get_distances()
        vertices = self.get_vertices()


        for u in vertices:
            distances[u][u] = 0
            if u in self.graph:
                for v, w in self.graph[u]:
                    distances[u][v] = w
        

        for k in vertices:
            for i in vertices:
                for j in vertices:
                    if distances[i][k] != float("inf") and distances[k][j] != float("inf"):
                        distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        return distances

if __name__ == "__main__":
    g = Graph()
    g.add_edge("a", "b", 10)
    g.add_edge("a", "c", 9)
    g.add_edge("b", "c", 8)
    g.add_edge("c", "d", -20)
    g.add_edge("c", "e", 10)
    g.add_edge("e", "d", 5)
    distances = g.floyed_warshell_shortest_path()
    print(distances)

        
