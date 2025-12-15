import matplotlib.pyplot as plt
import networkx as nx


# =========================
# Visualize Minimum Spanning Tree
# =========================
def visualize_mst(vertices, all_edges, mst_edges, algorithm_name):
    G = nx.Graph()
    G.add_nodes_from(range(vertices))
    for u, v, w in all_edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)

    fig = plt.figure(figsize=(9, 7))
    fig.canvas.manager.set_window_title(f"{algorithm_name} Algorithm")

    nx.draw_networkx_edges(G, pos, edge_color="gray", alpha=0.6)
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=800)
    nx.draw_networkx_labels(G, pos, font_size=14, font_weight="bold")
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels={(u, v): w for u, v, w in all_edges},
        font_color="gray"
    )

    mst_edge_list = [(u, v) for u, v, _ in mst_edges]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edge_list,
                           edge_color="red", width=3)

    plt.axis("off")
    plt.tight_layout()
    plt.show()


# =========================
# Visualize Maximum Flow (Edmonds–Karp)
# =========================
def visualize_flow_network(network, source, sink, max_flow, flow_matrix, augmenting_paths=None):
    G = nx.DiGraph()
    for u in range(network.V):
        for v in range(network.V):
            capacity = network.graph[u][v]
            if capacity > 0:
                G.add_edge(u, v, capacity=capacity, flow=flow_matrix[u][v])

    pos = nx.spring_layout(G, seed=42)

    fig = plt.figure(figsize=(9, 7))
    fig.canvas.manager.set_window_title("Edmonds–Karp's Algorithm")

    nx.draw(
        G, pos,
        with_labels=True,
        node_color="lightgreen",
        node_size=1200,
        font_size=16,
        font_weight="bold",
        arrows=True,
        arrowstyle="->",
        arrowsize=25
    )

    edge_labels = {
        (u, v): f"{d['flow']}/{d['capacity']}"
        for u, v, d in G.edges(data=True)
        if d["flow"] > 0
    }
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=edge_labels,
        font_color="blue",
        font_size=14,
        bbox=dict(facecolor="white", edgecolor="none", pad=0.2),
        label_pos=0.5
    )

    

    if augmenting_paths:
        last_path = augmenting_paths[-1]
        nx.draw_networkx_edges(
            G, pos,
            edgelist=last_path,
            edge_color="red",
            width=5,
            arrowstyle="->",
            arrowsize=30
        )

    plt.axis("off")
    plt.tight_layout()
    plt.show()
