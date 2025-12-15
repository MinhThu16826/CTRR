def dfs(adj, s):
    n = len(adj)
    visited = [False] * n
    order = []

    def visit(u):
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visit(v)

    visit(s)
    return order