# bfs_visualize.py
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def visualize_bfs(adj, start):
    G = nx.Graph()

    # Tạo đồ thị
    for u in range(len(adj)):
        for v in adj[u]:
            G.add_edge(u, v)

    pos = nx.spring_layout(G, seed=42)

    visited = [False] * len(adj)
    q = deque([start])
    visited[start] = True

    while q:
        u = q.popleft()

        colors = []
        for i in range(len(adj)):
            if i == u:
                colors.append("red")       # node đang xét
            elif visited[i]:
                colors.append("yellow")    # đã thăm
            else:
                colors.append("lightgray") # chưa thăm

        plt.figure(figsize=(6, 4))
        nx.draw(G, pos, with_labels=True,
                node_color=colors,
                node_size=800)

        plt.title(f"BFS – Đang duyệt đỉnh {u}")
        plt.show()

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

# chạy thử
if __name__ == "__main__":
    adj = [
        [1, 2],
        [0, 3],
        [0, 3],
        [1, 2]
    ]
    visualize_bfs(adj, 0)

