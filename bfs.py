from collections import deque

def bfs(adj, s):
    n = len(adj)
    visited = [False] * n
    dist = [-1] * n
    parent = [-1] * n
    order = []

    q = deque([s])
    visited[s] = True
    dist[s] = 0

    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                dist[v] = dist[u] + 1
                q.append(v)

    return {
        "order": order,
        "dist": dist,
        "parent": parent
    }