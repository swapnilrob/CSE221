import sys
input = sys.stdin.readline
 
inversion_count = 0  
 
def merge(left, right):
    global inversion_count
    merged = []
    i = j = 0
 
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            inversion_count += len(left) - i 
            merged.append(right[j])
            j += 1
 
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
 
 
n = int(input())
A = list(map(int, input().split()))
sorted_A = merge_sort(A)
print(inversion_count)
print(*sorted_A)