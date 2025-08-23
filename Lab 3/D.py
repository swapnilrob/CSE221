import sys
input = sys.stdin.read
 
MOD = 10**9 + 7
 
def multiply(A, B):
    return [
        [
            (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
            (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD
        ],
        [
            (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
            (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD
        ]
    ]
 
def matrix_power(matrix, power):
    result = [[1, 0], [0, 1]]  
    while power:
        if power % 2:
            result = multiply(result, matrix)
        matrix = multiply(matrix, matrix)
        power //= 2
    return result
 
 
data = input().split()
idx = 0
T = int(data[idx])
idx += 1
output = []
 
for i in range(T):
    a11 = int(data[idx])
    a12 = int(data[idx + 1])
    a21 = int(data[idx + 2])
    a22 = int(data[idx + 3])
    idx += 4
    X = int(data[idx])
    idx += 1
 
    matrix = [[a11, a12], [a21, a22]]
    result = matrix_power(matrix, X)
 
    output.append(f"{result[0][0]} {result[0][1]}")
    output.append(f"{result[1][0]} {result[1][1]}")
 
 
sys.stdout.write('\n'.join(output) + '\n')