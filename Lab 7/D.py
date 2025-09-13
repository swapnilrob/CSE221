import sys
import heapq

data = sys.stdin.read().split()
n, m, s, d = map(int, data[:4])
w = [0] + list(map(int, data[4:4+n]))
edges = list(map(int, data[4+n:]))

g = [[] for _ in range(n+1)]
for i in range(m):
    u, v = edges[2*i], edges[2*i+1]
    g[u].append(v)

dist = [float('inf')] * (n+1)
dist[s] = w[s]
pq = [(w[s], s)]

while pq:
    cost, u = heapq.heappop(pq)
    if cost != dist[u]:
        continue
    for v in g[u]:
        new_cost = cost + w[v]
        if new_cost < dist[v]:
            dist[v] = new_cost
            heapq.heappush(pq, (new_cost, v))

print(dist[d] if dist[d] != float('inf') else -1)
