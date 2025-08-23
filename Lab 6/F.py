import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m, s, q = map(int, input().split())
    adj = [[] for i in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    sources = list(map(int, input().split()))
    destinations = list(map(int, input().split()))
    
    dist = [-1] * (n + 1)
    dq = deque()
    
    for src in sources:
        dist[src] = 0
        dq.append(src)
    
    while dq:
        node = dq.popleft()
        for nei in adj[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + 1
                dq.append(nei)
    
    result = [str(dist[d]) for d in destinations]
    print(" ".join(result))

solve()
