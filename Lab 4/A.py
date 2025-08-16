def adjacency_matrix_representation(N,M):
    adj_mat= [[0]*N for i in range(N)]
    
    for j in range(M):
        u,v,w= map(int, input().split())
        adj_mat[u-1][v-1]=w

    for row in adj_mat:
        print(*row)

N,M= map(int, input().split())
adjacency_matrix_representation(N,M)
