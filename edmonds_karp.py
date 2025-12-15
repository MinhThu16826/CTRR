from collections import deque

def edmonds_karp(network: 'FlowNetwork', source: int, sink: int):
    V = network.V
    max_flow = 0
    augmenting_paths = []  # Store each augmenting path as list of edges (u, v)

    while True:
        # BFS to find augmenting path
        parent = [-1] * V
        visited = [False] * V
        queue = deque([source])
        visited[source] = True

        found_path = False
        while queue and not found_path:
            u = queue.popleft()
            for v in range(V):
                residual_capacity = network.graph[u][v] - network.flow[u][v]
                if not visited[v] and residual_capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        found_path = True
                        break

        if not found_path:
            break  # No more augmenting path

        # Find minimum capacity along the path
        path_flow = float('inf')
        v = sink
        path_edges = []  # List of (u, v) edges in forward direction
        while v != source:
            u = parent[v]
            path_edges.append((u, v))
            residual = network.graph[u][v] - network.flow[u][v]
            path_flow = min(path_flow, residual)
            v = u

        path_edges.reverse()  # From source to sink
        augmenting_paths.append(path_edges)  # Only store the list of edges

        # Update residual capacities and flow
        v = sink
        while v != source:
            u = parent[v]
            network.flow[u][v] += path_flow
            network.flow[v][u] -= path_flow  # Reverse edge (residual)
            v = u

        max_flow += path_flow

    return max_flow, augmenting_paths, network.flow