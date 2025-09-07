import sys
input = sys.stdin.readline

n, k = map(int, input().split())
parent = [i for i in range(n+1)]
size = [1] * (n+1)

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]  
        u = parent[u]
    return u

def union(u, v):
    u_root, v_root = find(u), find(v)
    if u_root == v_root:
        return size[u_root]
    if size[u_root] < size[v_root]:
        u_root, v_root = v_root, u_root
    parent[v_root] = u_root
    size[u_root] += size[v_root]
    return size[u_root]

out = []
for _ in range(k):
    a, b = map(int, input().split())
    out.append(str(union(a, b)))

sys.stdout.write("\n".join(out))
