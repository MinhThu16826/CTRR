import heapq
from undirected_graph import UndirectedGraph

# Prim's MST
def prim_mst(graph):
    V = graph.V
    key = [float('inf')] * V
    parent = [-1] * V
    key[0] = 0
    pq = [(0, 0)]  # (key, vertex)
    mst_set = [False] * V

    while pq:
        u = heapq.heappop(pq)[1]
        if mst_set[u]:
            continue
        mst_set[u] = True
        for weight, v in graph.graph[u]:
            if not mst_set[v] and key[v] > weight:
                key[v] = weight
                parent[v] = u
                heapq.heappush(pq, (key[v], v))

    mst_edges = [(parent[i], i, key[i]) for i in range(1, V) if parent[i] != -1]
    return mst_edges