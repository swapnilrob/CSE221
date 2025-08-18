import sys
sys.setrecursionlimit(200005)

def solve():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)

    state = [0] * (n + 1)

    def has_cycle_dfs(node):
        state[node] = 1
        
        for neighbor in adj[node]:
            if state[neighbor] == 1:
                return True
            if state[neighbor] == 0:
                if has_cycle_dfs(neighbor):
                    return True        
        state[node] = 2
        return False
    for i in range(1, n + 1):
        if state[i] == 0:
            if has_cycle_dfs(i):
                print("YES")
                return
            
    print("NO")

solve()
