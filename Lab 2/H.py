def kth_not_divisible(k, x):
    low = 1
    high = 2 * k
    result = -1
 
    while low <= high:
        mid = (low + high) // 2
        count = mid - (mid // x)
        if count >= k:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
 
    return result
 
T = int(input())
for _ in range(T):
    k_val, x_val = map(int, input().split())
    print(kth_not_divisible(k_val, x_val))