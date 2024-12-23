class Graph:
    def __init__(self):
        self.graph = {}

    def _add_if_not_present(self, node):
        if node not in self.graph:
            self.graph[node] = []
    def add_edge(self, u, v, weight):
        self._add_if_not_present(u) 
        self.graph[u].append((v, weight))

    def get_all_nodes(self):
        distances = {i:float("inf") for i in self.graph}
        for i in self.graph.values():
            for j, _ in i:
                if j not in distances:
                    distances[j] = float("inf")
        print(distances)
        return distances


    def bellman_ford_shortest_path(self, source):
        distances = self.get_all_nodes()
        distances[source] = 0
        parent = {}

        # for _ in range(len(self.graph) - 1):
        for u in self.graph:
            for v, weight in self.graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    parent[v] = u

        for u in self.graph:
            for v, weight in self.graph[u]:
                print(distances[u] + weight < distances[v])
                if distances[u] + weight < distances[v]:
                    raise ValueError("negative weight cycel detected")

        return distances, parent

    def get_path(self, parent, dest):
        path = []
        current = dest
        while current:
            path.append(current)
            if current not in parent:
                break
            current = parent[current]
            
        return path[::-1]

if __name__ == "__main__":
    g = Graph()
    g.add_edge("a", "b", 10)
    g.add_edge("a", "c", 9)
    g.add_edge("b", "c", 8)
    g.add_edge("c", "d", 20)
    g.add_edge("c", "e", 10)
    g.add_edge("e", "d", 5)
         
    distances, parent = g.bellman_ford_shortest_path("a")
    print(distances, parent)
    path = g.get_path(parent, "d")
    print(path)
