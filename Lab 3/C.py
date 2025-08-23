import sys
input = sys.stdin.readline
 
def mod_exp(a, b, mod=107):
    result = 1
    a %= mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result
 
a, b = map(int, input().split())
print(mod_exp(a, b))