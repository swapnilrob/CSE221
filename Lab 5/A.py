from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for edges in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
order = []
queue = deque([1])
visited[1] = True

while queue:
    u = queue.popleft()
    order.append(u)
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            queue.append(v)

print(*order)