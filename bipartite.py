from collections import deque

def is_bipartite(adj):
    n = len(adj)
    color = [-1] * n

    for s in range(n):
        if color[s] != -1:
            continue

        q = deque([s])
        color[s] = 0

        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False, color

    return True, color