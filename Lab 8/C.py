import sys
sys.setrecursionlimit(1000000)

data = list(map(int, sys.stdin.read().split()))
it = iter(data)
n = next(it); m = next(it)

edges = []
for i in range(m):
    u = next(it); v = next(it); w = next(it)
    edges.append((w, u, v, i))
parent = list(range(n+1))
rank = [0]*(n+1)
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    a = find(a); b = find(b)
    if a == b: return False
    if rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
    return True

edges_sorted = sorted(edges, key=lambda e: e[0])
used = [False]*m
mst_cost = 0
mst_edges_count = 0
adj = [[] for _ in range(n+1)]

for w,u,v,idx in edges_sorted:
    if union(u, v):
        used[idx] = True
        mst_cost += w
        mst_edges_count += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
if mst_edges_count != n-1:
    print(-1)
    sys.exit(0)
LOG = (n).bit_length() + 1
up = [[-1]*(n+1) for _ in range(LOG)]
max1 = [[-1]*(n+1) for _ in range(LOG)]  
max2 = [[-1]*(n+1) for _ in range(LOG)]  
depth = [0]*(n+1)
stack = [(1, 0, -1, -1)] 
visited = [False]*(n+1)
while stack:
    node, dep, par, wpar = stack.pop()
    if visited[node]:
        continue
    visited[node] = True
    depth[node] = dep
    up[0][node] = par
    max1[0][node] = wpar
    max2[0][node] = -1
    for nei, wt in adj[node]:
        if not visited[nei]:
            stack.append((nei, dep+1, node, wt))

def merge_pair(a1, a2, b1, b2):
    cand = [a1, a2, b1, b2]
    best = -1
    for x in cand:
        if x > best:
            best = x
    sec = -1
    for x in cand:
        if x != best and x > sec:
            sec = x
    return best, sec
for k in range(1, LOG):
    for v in range(1, n+1):
        mid = up[k-1][v]
        if mid != -1:
            up[k][v] = up[k-1][mid]
            b1, b2 = max1[k-1][mid], max2[k-1][mid]
            a1, a2 = max1[k-1][v], max2[k-1][v]
            m1, m2 = merge_pair(a1, a2, b1, b2)
            max1[k][v], max2[k][v] = m1, m2

def get_top_two_on_path(u, v):
    if u == v:
        return -1, -1
    m1 = -1; m2 = -1
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    k = 0
    while diff:
        if diff & 1:
            m1, m2 = merge_pair(m1, m2, max1[k][u], max2[k][u])
            u = up[k][u]
        diff >>= 1
        k += 1
    if u == v:
        return m1, m2
    for k in range(LOG-1, -1, -1):
        if up[k][u] != -1 and up[k][u] != up[k][v]:
            m1, m2 = merge_pair(m1, m2, max1[k][u], max2[k][u])
            m1, m2 = merge_pair(m1, m2, max1[k][v], max2[k][v])
            u = up[k][u]
            v = up[k][v]
    m1, m2 = merge_pair(m1, m2, max1[0][u], max2[0][u])
    m1, m2 = merge_pair(m1, m2, max1[0][v], max2[0][v])
    return m1, m2

second_best = None
for w,u,v,idx in edges:
    if used[idx]:
        continue
    m1, m2 = get_top_two_on_path(u, v)
    if m1 == -1:
        continue
    if w > m1:
        cand = mst_cost + w - m1
        if cand > mst_cost:
            if second_best is None or cand < second_best:
                second_best = cand
    elif w == m1:
        if m2 != -1:
            cand = mst_cost + w - m2
            if cand > mst_cost:
                if second_best is None or cand < second_best:
                    second_best = cand
    else: 
        cand = mst_cost + w - m1
        if cand > mst_cost:
            if second_best is None or cand < second_best:
                second_best = cand

print(second_best if second_best is not None else -1)
