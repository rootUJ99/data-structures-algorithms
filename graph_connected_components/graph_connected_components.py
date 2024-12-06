class UnionFind():
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = size
        
    def find(self, x):
        if self.parent[x]!= x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x1 = self.find(x)
        y1 = self.find(y)

        if x1 == y1:
            return

        if self.rank[x1] < self.rank[y1]:
            self.parent[x1] = self.parent[y1]
        if self.rank[x1] > self.rank[y1]:
            self.parent[y1] = self.parent[x1]
        else:
            self.parent[y1] = x1
            self.rank[x1]+=1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class GraphConnectedComponents():
    def __init__(self, uf):
        self.graph = {}
        self.uf = uf

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def vertex_count(self):
        vertices = set(list(self.graph.keys()))

        return [*vertices]

    def connected_components(self):
        group = set()
        vertices = self.vertex_count()

        for i in self.graph:
            for j in self.graph[i]: 
                node = tuple(sorted([i, j]))
                if node in group:
                    continue
                group.add(node)
                uf.union(i, j)
        
        connected = {}
        for vertex in vertices:
            root = uf.find(vertex)
            if root not in connected:
                connected[root] = []
            connected[root].append(vertex)
        
        return connected

if __name__ == "__main__":
    uf = UnionFind(10) 
    g = GraphConnectedComponents(uf)
    graph_edges = [(1, 2) ,(1, 3), (3, 4),(3, 5), (6, 7),(6, 8)]
    for node in graph_edges:
        u, v = node
        g.add_edge(u, v)
    connected_components = g.connected_components()
    print("graph", g.graph)
    print("connected compoenents", g.connected_components())

