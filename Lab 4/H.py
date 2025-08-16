from math import gcd

def coprime_graph_queries(n, q):
    graph = [[] for r in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1): 
            if gcd(i, j) == 1:
                graph[i].append(j)
                graph[j].append(i)

    for i in range(1, n + 1):
        graph[i].sort()

    for s in range(q):
        x, k = map(int, input().split())
        if k <= len(graph[x]):
            print(graph[x][k - 1])
        else:
            print(-1)

n, q = map(int, input().split())
coprime_graph_queries(n, q)
