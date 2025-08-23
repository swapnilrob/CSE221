def max_subarray_length(n, k, arr):
    left = 0
    current_sum = 0
    max_len = 0
 
    for right in range(n):
        current_sum += arr[right]
 
        while current_sum > k:
            current_sum -= arr[left]
            left += 1
 
        max_len = max(max_len, right - left + 1)
 
    return max_len
 
n, k = map(int, input().split())
arr = list(map(int, input().split())) 
print(max_subarray_length(n, k, arr))