def adjacency_list_representation(n, m):

    dic1 = {i + 1: [] for i in range(n)}
    
    u_nodes = list(map(int, input().split()))
    v_nodes = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    
    for i in range(m):
        dic1[u_nodes[i]].append((v_nodes[i], weights[i]))

    for node in range(1, n + 1):
        if dic1[node]:
            print(f"{node}:", *dic1[node])
        else:
            print(f"{node}:")

n, m = map(int, input().split())
adjacency_list_representation(n, m)