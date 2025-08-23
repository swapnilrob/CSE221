def max_k_distinct_subarray(n, k, nums):
    freq = {}
    start = 0
    max_len = 0
 
    for end in range(n):
        value = nums[end]
        if value in freq:
            freq[value] += 1
        else:
            freq[value] = 1
 
        while len(freq) > k:
            removing = nums[start]
            freq[removing] -= 1
            if freq[removing] == 0:
                del freq[removing]
            start += 1
 
        max_len = max(max_len, end - start + 1)
 
    return max_len
 
n, k = map(int, input().split())
array = list(map(int, input().split()))
 
print(max_k_distinct_subarray(n, k, array))