import sys
import heapq
data = sys.stdin.read().split()
n, m = map(int, data[:2])
edges = list(map(int, data[2:]))

g = [[] for _ in range(n+1)]
for i in range(m):
    u, v, w = edges[3*i], edges[3*i+1], edges[3*i+2]
    g[u].append((v, w))
    g[v].append((u, w))

danger = [float('inf')] * (n+1)
danger[1] = 0
pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    if d != danger[u]:
        continue
    for v, w in g[u]:
        nd = max(d, w)         
        if nd < danger[v]:
            danger[v] = nd
            heapq.heappush(pq, (nd, v))

res = []
for i in range(1, n+1):
    res.append(str(danger[i] if danger[i] != float('inf') else -1))
print(" ".join(res))
