import heapq


class DirectedGraph():
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        self.graph[v] = [] 

    def add_edge(self, v1, v2, weight):
        if v1 not in self.graph:
            self.graph[v1] = []


        self.graph[v1].append((v2, weight))
    
    def dfs(self, vertex):
        visited = []
        stack = []
        stack.append(vertex)
        while len(stack) > 0:
            current_vertex = stack.pop()
            visited.append(current_vertex)
            if current_vertex not in self.graph:
                continue
            for neighbour in self.graph[current_vertex]:
                node, _ = neighbour
                if node in visited:
                    continue
                stack.append(node)
        return visited
                
    def get_distances(self):
        distances = {}
        for key, value in self.graph.items():
            distances[key] = float("inf")
            for v in value:
                if v[0] not in distances:
                    distances[v[0]] = float("inf")
        return distances

    def dijkstras_shortest_path(self, start_vertex):
        distances = self.get_distances()
        distances[start_vertex] = 0
        paths = {i:[] for i in self.graph}

        paths[start_vertex] = [start_vertex]
        pq = [(0, start_vertex)]

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)
            print(pq)
            
            if current_dist > distances[current_vertex]:
                continue

            if current_vertex not in self.graph:
                continue

            for neighbour in self.graph[current_vertex]:
                neighbour_vertex, neighbour_dist = neighbour

                distance_from_start_node = neighbour_dist + current_dist
                if distance_from_start_node < distances[neighbour_vertex]:
                    distances[neighbour_vertex] = distance_from_start_node
                    paths[neighbour_vertex] = paths[current_vertex] + [neighbour_vertex]

                    heapq.heappush(pq, (distance_from_start_node, neighbour_vertex))
        return distances, paths


if __name__ == "__main__":
    g = DirectedGraph()
    g.add_edge("a", "b", 4)
    g.add_edge("b", "c", 2)
    g.add_edge("c", "d", 3)
    g.add_edge("a", "e", 5)
    g.add_edge("e", "d", 7)
    g.add_edge("b", "f", 3)
    g.add_edge("f", "d", 3)
    visited = g.dfs([*g.graph.keys()][0]) 
    distances,paths = g.dijkstras_shortest_path("a")


    for key in distances:
        print("shortest path from", key, "is", distances[key], "with path", "->".join(paths[key]))
