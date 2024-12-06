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

    def get_vertices(self):
        vertices = set(list(self.graph.keys()))

        return [*vertices]

    def dfs(self, start):
        stack = []
        visited = set()
        stack.append(start)
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for subnode in self.graph[node]:
                if subnode not in visited:
                    stack.append(subnode)

        return [*visited]

    def connected_compoennts_dfs(self):
        all_visited = set()
        group = [] 
        for node in self.get_vertices():
            if node in all_visited:
                continue
            components = self.dfs(node)
            group.append(components)
            all_visited.update(components)

        return group

    def connected_components_unionfind(self):
        group = set()
        vertices = self.get_vertices()

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
    connected_components_with_unionfind = g.connected_components_unionfind()

    connected_components_with_dfs = g.connected_compoennts_dfs()

    print("graph", g.graph)
    print("connected compoenents with union find", connected_components_with_unionfind)
    print("connected compoenents with dfs", connected_components_with_dfs)

