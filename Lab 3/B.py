import sys
input = sys.stdin.readline
 
count = 0  # Global counter
 
def merge(left, right):
    global count
    merged = []
    i = j = 0
    right_squares = sorted([x * x for x in right])
 
    for val in left:
        if val > 0:
            low, high = 0, len(right_squares)
            while low < high:
                mid = (low + high) // 2
                if right_squares[mid] < val:
                    low = mid + 1
                else:
                    high = mid
            count += low
 
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
 
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
 
n = int(input())
arr = list(map(int, input().split()))
merge_sort(arr)
print(count)