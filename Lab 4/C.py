def meramorphosis(n):
    matrix = [[0] * n for i in range(n)]
    
    for j in range(n):
        data = list(map(int, input().split()))
        #k = data[0]         
        neighbors = data[1:] 
        for v in neighbors:
            matrix[j][v] = 1  

    for row in matrix:
        print(*row)

n = int(input())
meramorphosis(n)
