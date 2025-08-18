import sys
sys.setrecursionlimit(2 * 10**5 + 5) 
def solve():
    n_str, r_str = sys.stdin.readline().split()
    n = int(n_str)
    r = int(r_str)
    
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        u_str, v_str = sys.stdin.readline().split()
        u = int(u_str)
        v = int(v_str)
        adj[u].append(v)
        adj[v].append(u)
        
    q = int(sys.stdin.readline())
    
    queries = [int(sys.stdin.readline()) for _ in range(q)]

    subtree_sizes = [0] * (n + 1)

    def dfs(u, parent):
        count = 1  
        
        for v in adj[u]:
            if v != parent:
                count += dfs(v, u)
        
        subtree_sizes[u] = count
        
        return count

    dfs(r, -1)

    for x in queries:
        print(subtree_sizes[x])

if __name__ == "__main__":
    solve()