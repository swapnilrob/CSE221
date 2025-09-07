import sys
input = sys.stdin.readline

n,m = map(int, input().split())
edges = []
total = 0

for i in range (m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
    total += w
parent = [i for i in range(n+1)]
size = [1]*(n+1)

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(u, v):
    u, v = find(u), find(v)
    if u == v: return False
    if size[u] < size[v]:
        u, v = v, u
    parent[v] = u
    size[u] += size[v]
    return True

edges.sort()
mst_cost = 0
for w, u, v in edges:
    if union(u, v):
        mst_cost += w

print(mst_cost)
