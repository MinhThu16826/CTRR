
import heapq

def dijkstra(graph, start, end):
    dist = {v: float("inf") for v in graph.adj}
    parent = {v: None for v in graph.adj}

    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        if u == end:
            break

        for v, w in graph.adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    if dist[end] == float("inf"):
        return None, []

    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return dist[end], path
