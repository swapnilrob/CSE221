from collections import deque

def max_group(n, m):
    graph = [[] for i in range(n + 1)]
    for j in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * (n + 1)
    answer = 0

    for start in range(1, n + 1):
        if color[start] == -1:
            q = deque([start])
            color[start] = 0
            cnt = [1, 0]  
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        cnt[color[v]] += 1
                        q.append(v)
                    elif color[v] == color[u]:
                        print(-1)
                        return

            answer += max(cnt[0], cnt[1])

    print(answer)


n, m = map(int, input().split())
max_group(n, m)
