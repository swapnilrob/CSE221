import sys
import heapq

def dijkstra(n, start, g):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        du, u = heapq.heappop(pq)
        if du != dist[u]:
            continue
        for v, w in g[u]:
            if dist[v] > du + w:
                dist[v] = du + w
                heapq.heappush(pq, (dist[v], v))
    return dist

input_data = sys.stdin.read().split()
n, m, s, t = map(int, input_data[:4])
edges = list(map(int, input_data[4:]))

g = [[] for _ in range(n+1)]
for i in range(m):
    u, v, w = edges[3*i], edges[3*i+1], edges[3*i+2]
    g[u].append((v, w))

dist_s = dijkstra(n, s, g)
dist_t = dijkstra(n, t, g)

best_time = float('inf')
best_node = -1

for node in range(1, n+1):
    if dist_s[node] != float('inf') and dist_t[node] != float('inf'):
        time = max(dist_s[node], dist_t[node]) 
        if time < best_time or (time == best_time and node < best_node):
            best_time = time
            best_node = node

if best_node == -1:
    print(-1)
else:
    print(best_time, best_node)
