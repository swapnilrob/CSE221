import sys
import heapq

def read_input():
    data = sys.stdin.read().split()
    n, m, s, d = map(int, data[:4])
    u = list(map(int, data[4:4+m]))
    v = list(map(int, data[4+m:4+2*m]))
    w = list(map(int, data[4+2*m:4+3*m]))
    return n, m, s, d, u, v, w

def build_graph(n, m, u, v, w):
    g = [[] for _ in range(n+1)]
    for i in range(m):
        g[u[i]].append((v[i], w[i]))
    return g

def dijkstra(n, s, d, g):
    dist = [float('inf')] * (n+1)
    parent = [-1] * (n+1)
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        du, u = heapq.heappop(pq)
        if du != dist[u]:
            continue
        if u == d:
            break
        for nxt, w in g[u]:
            if dist[nxt] > du + w:
                dist[nxt] = du + w
                parent[nxt] = u
                heapq.heappush(pq, (dist[nxt], nxt))
    return dist, parent

def reconstruct_path(parent, s, d):
    path = []
    cur = d
    while cur != -1:
        path.append(cur)
        if cur == s:
            break
        cur = parent[cur]
    if path[-1] != s:
        return []
    path.reverse()
    return path

n, m, s, d, u, v, w = read_input()
g = build_graph(n, m, u, v, w)
dist, parent = dijkstra(n, s, d, g)

if dist[d] == float('inf'):
    print(-1)
else:
    print(dist[d])
    path = reconstruct_path(parent, s, d)
    print(*path)
