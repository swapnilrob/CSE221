
import sys
input = sys.stdin.readline
 
def fast_series(a, n, m):
    if a == 1:
        return n % m
    
    a_minus_1 = a - 1
    mod = m * a_minus_1  
    exp = n + 1
    a_pow = pow(a, exp, mod)
    numerator = (a_pow - a) % mod
    sum_mod = (numerator // a_minus_1) % m
    return sum_mod
 
T = int(input())
for i in range(T):
    a, n, m = map(int, input().split())
    print(fast_series(a, n, m))