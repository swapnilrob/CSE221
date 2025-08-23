def merge_sorted_lists(n, list_a, m, list_b):
    merged = []
    idx_a = 0
    idx_b = 0
 
    while idx_a < n and idx_b < m:
        if list_a[idx_a] <= list_b[idx_b]:
            merged.append(list_a[idx_a])
            idx_a += 1
        else:
            merged.append(list_b[idx_b])
            idx_b += 1
 
    while idx_a < n:
        merged.append(list_a[idx_a])
        idx_a += 1
    while idx_b < m:
        merged.append(list_b[idx_b])
        idx_b += 1
 
    return merged
 
n = int(input())
list_a = list(map(int, input().split()))
m = int(input())
list_b = list(map(int, input().split()))
 
result = merge_sorted_lists(n, list_a, m, list_b)
print(' '.join(str(num) for num in result))