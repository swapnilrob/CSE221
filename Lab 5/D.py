from collections import deque

def bfs(start, n, graph):
    dist = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    q = deque([start])
    dist[start] = 0
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)
    return dist, parent

def reconstruct_path(parent, start, end):
    if parent[end] == -1 and start != end:
        return []
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]
    if path[-1] != start:
        return []
    return path[::-1]

n, m, S, D, K = map(int, input().split())
graph = [[] for i in range(n + 1)]
for j in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

distS, parentS = bfs(S, n, graph)
distK, parentK = bfs(K, n, graph)

if distS[K] == -1 or distK[D] == -1:
    print(-1)
else:
    path1 = reconstruct_path(parentS, S, K)
    path2 = reconstruct_path(parentK, K, D)
    if not path1 or not path2:
        print(-1)
    else:
        full_path = path1 + path2[1:]   
        print(len(full_path) - 1)
        print(*full_path)
