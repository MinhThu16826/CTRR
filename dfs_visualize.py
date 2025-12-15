# dfs_visualize.py
import networkx as nx
import matplotlib.pyplot as plt

def visualize_dfs(adj, start):
    G = nx.Graph()

    for u in range(len(adj)):
        for v in adj[u]:
            G.add_edge(u, v)

    pos = nx.spring_layout(G, seed=42)
    visited = [False] * len(adj)

    def dfs(u):
        visited[u] = True

        colors = []
        for i in range(len(adj)):
            if i == u:
                colors.append("orange")       # node đang xét
            elif visited[i]:
                colors.append("lightgreen")
            else:
                colors.append("blue")

        plt.figure(figsize=(6, 4))
        nx.draw(G, pos, with_labels=True,
                node_color=colors,
                node_size=800)

        plt.title(f"DFS – Đang duyệt đỉnh {u}")
        plt.show()

        for v in adj[u]:
            if not visited[v]:
                dfs(v)

    dfs(start)

# chạy thử
if __name__ == "__main__":
    adj = [
        [1, 2],
        [0, 3],
        [0, 3],
        [1, 2]
    ]
    visualize_dfs(adj, 0)
