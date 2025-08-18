from collections import deque

def build_graph(n, u_list, v_list):
    graph = [[] for _ in range(n + 1)]
    for u, v in zip(u_list, v_list):
        graph[u].append(v)
        graph[v].append(u)
    for adj in graph:
        adj.sort()
    return graph


def bfs_shortest_path(n, graph, start, dest):
    dist = [-1] * (n + 1)      
    parent = [-1] * (n + 1)    

    queue = deque([start])
    dist[start] = 0

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1:  
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)

    if dist[dest] == -1:      
        return -1, []
    path = []
    cur = dest
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return dist[dest], path



n, m, S, D = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
graph = build_graph(n, u_list, v_list)
distance, path = bfs_shortest_path(n, graph, S, D)

if distance == -1:
    print(-1)
else:
    print(distance)       
    print(*path)         