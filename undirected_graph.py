from collections import defaultdict

# Undirected weighted graph
class UndirectedGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)  # (weight, vertex)

    def add_edge(self, u, v, w):
        self.graph[u].append((w, v))
        self.graph[v].append((w, u))