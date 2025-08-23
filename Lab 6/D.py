import sys
from collections import deque

def tree_diameter(n, edges):
    g = [[] for i in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    def bfs(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        q = deque([start])
        far_node = start
        while q:
            u = q.popleft()
            for v in g[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
                    if dist[v] > dist[far_node]:
                        far_node = v
        return far_node, dist[far_node]

    a, dist_a = bfs(1)
    b, length = bfs(a)
    print(length)
    print(a, b)

input = sys.stdin.readline
n = int(input())
edges = [tuple(map(int, input().split())) for j in range(n - 1)]
tree_diameter(n, edges)
