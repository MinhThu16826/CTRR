from undirected_graph import UndirectedGraph
from prim import prim_mst
from kruskal import kruskal_mst
from flow_network import FlowNetwork
from edmonds_karp import edmonds_karp
from visualize import visualize_mst, visualize_flow_network
import matplotlib.pyplot as plt
plt.close('all')
if __name__ == "__main__":
    # MST Example
    g = UndirectedGraph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    all_edges = [(0,1,2), (0,3,6), (1,2,3), (1,3,8), (1,4,5), (2,4,7), (3,4,9)]

    prim_edges = prim_mst(g)
    visualize_mst(5, all_edges, prim_edges, "Prim's")

    kruskal_edges = kruskal_mst(g)
    visualize_mst(5, all_edges, kruskal_edges, "Kruskal's")

    # Max Flow Example
    fn = FlowNetwork(6)
    fn.add_edge(0, 1, 16)
    fn.add_edge(0, 2, 13)
    fn.add_edge(1, 2, 10)
    fn.add_edge(1, 3, 12)
    fn.add_edge(2, 1, 4)
    fn.add_edge(2, 4, 14)
    fn.add_edge(3, 2, 9)
    fn.add_edge(3, 5, 20)
    fn.add_edge(4, 3, 7)
    fn.add_edge(4, 5, 4)

    max_flow, augmenting_paths, flow_matrix = edmonds_karp(fn, 0, 5)
    print(f"Max Flow: {max_flow}")
    visualize_flow_network(fn, 0, 5, max_flow, flow_matrix, augmenting_paths)