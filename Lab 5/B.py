n, m = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

graph = [[] for i in range(n + 1)]
for u, v in zip(u_list, v_list):
    graph[u].append(v)
    graph[v].append(u)

for adj in graph:
    adj.sort(reverse=True)  
visited = [False] * (n + 1)
order = []

stack = [1]              
while stack:
    u = stack.pop()
    if not visited[u]:
        visited[u] = True
        order.append(u)
        for v in graph[u]:
            if not visited[v]:
                stack.append(v)

print(*order)
