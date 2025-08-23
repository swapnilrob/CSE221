from collections import deque

def course_order(n, m):
    graph = [[] for i in range(n + 1)]
    indegree = [0] * (n + 1)

    for j in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    q = deque()
    for k in range(1, n + 1):
        if indegree[k] == 0:
            q.append(k)

    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    if len(order) < n:
        print(-1)
    else:
        print(*order)


n, m = map(int, input().split())
course_order(n, m)
