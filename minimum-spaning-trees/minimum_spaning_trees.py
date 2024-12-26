import heapq

class UnionFind():
    def __init__(self, vertices):
        self.parent = {u:u for u in vertices}
        self.rank = {u:0 for u in vertices}

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        f_x = self.find(u)
        f_y = self.find(v)
        if self.rank[f_x] < self.rank[f_y]:
            self.parent[f_x] = f_y
        elif self.rank[f_x] > self.rank[f_y]:
            self.parent[f_y] = f_x
        else:
            self.rank[f_x] +=1 
            self.parent[f_y] = f_x

class GraphMST():
    def __init__(self):
        self.graph = {}


    def check_if_present(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v, w):
        self.check_if_present(u) 
        self.check_if_present(v) 

        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def get_vertices(self):
        vertices = set([])
        for u in self.graph:
            vertices.add(u)
            for v, _ in self.graph[u]: 
                vertices.add(v)
        return list(vertices)
    
    def get_unique_edges(self):
        seen = set([])
        edges = []
        for u in self.graph:
            for v, w in self.graph[u]: 
                if (u,v) not in seen or (u,v) not in seen:
                    edges.append((w, u, v))
                    seen.add((u,v))
        edges.sort()

        return edges

    def mst_using_prims(self, start):
        visited = []
        mst_edges = []
        edges = [(weight, start, to) for to, weight in self.graph[start]]
        heapq.heapify(edges)
        visited.append(start)

        while edges:
            weight, old_start, to = heapq.heappop(edges)

            if to in visited:
                continue

            visited.append(to)
            mst_edges.append((old_start, to, weight))

            for new_start, weight in self.graph[to]:
                if new_start not in visited:
                    heapq.heappush(edges, (weight, to, new_start))

        return mst_edges


    def mst_using_kruskal(self):
        edges = self.get_unique_edges()

        uf = UnionFind(self.get_vertices())

        mst_edges = []
        for w, u, v in edges:
            if uf.find(u) != uf.find(v): 
                uf.union(u, v) 
                mst_edges.append((u, v, w))
        return mst_edges

        
if __name__ == "__main__":

    g  = GraphMST()
    g.add_edge("a", "b", 10)
    g.add_edge("a", "c", 9)
    g.add_edge("b", "c", 8)
    g.add_edge("c", "d", 20)
    g.add_edge("c", "e", 10)
    g.add_edge("e", "d", 5)
    mst_using_prims = g.mst_using_prims("a")
    mst_using_kruskal = g.mst_using_kruskal()
    print(mst_using_prims)
    print(mst_using_kruskal)

