def Two_Sum_Revisited(A, B, K, n, m):
    p1 = 0
    p2 = m - 1
    min_diff = float('inf')
    answer = (1, 1)
 
    while p1 < n and p2 >= 0:
        sum_val = int(A[p1]) + int(B[p2])
        current_diff = abs(sum_val - K)
 
        if current_diff < min_diff:
            min_diff = current_diff
            answer = (p1 + 1, p2 + 1)
 
        if sum_val == K:
            return f"{p1 + 1} {p2 + 1}"
        elif sum_val < K:
            p1 += 1
        else:
            p2 -= 1
 
    return f"{answer[0]} {answer[1]}"
 
line1 = input().split()
n = int(line1[0])
m = int(line1[1])
k = int(line1[2])
 
A = input().split()
B = input().split()
 
print(Two_Sum_Revisited(A, B, k, n, m))