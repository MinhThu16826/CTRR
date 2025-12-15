from union_find import UnionFind
from undirected_graph import UndirectedGraph

# Kruskal's MST
def kruskal_mst(graph):
    V = graph.V
    edges = []
    for u in graph.graph:
        for w, v in graph.graph[u]:
            if u < v:  # avoid duplicates
                edges.append((w, u, v))
    edges.sort()

    uf = UnionFind(V)
    mst_edges = []
    for w, u, v in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
    return mst_edges