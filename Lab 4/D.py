def seven_bridges(n, m):
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))

    degree = [0] * n

    for i in range(m):
        degree[u[i] - 1] += 1
        degree[v[i] - 1] += 1

    odd_count = 0
    for deg in degree:
        if deg % 2 != 0:
            odd_count += 1
    if odd_count == 0 or odd_count == 2:
        print("YES")
    else:
        print("NO")


n, m = map(int, input().split())
seven_bridges(n, m)
