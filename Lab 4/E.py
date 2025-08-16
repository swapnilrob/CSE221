def edge_queries(n, m):
    indegree = [0] * n
    outdegree = [0] * n

    u = list(map(int, input().split()))
    v = list(map(int, input().split()))

    for i in range(m):
        outdegree[u[i] - 1] += 1
        indegree[v[i] - 1] += 1

    result = [indegree[i] - outdegree[i] for i in range(n)]
    print(*result)


n, m = map(int, input().split())
edge_queries(n, m)
