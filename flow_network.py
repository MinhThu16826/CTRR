# Directed capacitated graph for max flow
class FlowNetwork:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]  # capacity
        self.flow = [[0] * vertices for _ in range(vertices)]  # flow

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity