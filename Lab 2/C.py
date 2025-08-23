
def attach_index(values):
    result = []
    for idx in range(len(values)):
        result.append((values[idx], idx + 1))
    return result
 
def find_three_sum(numbers, n, target_sum):
    numbered = attach_index(numbers)
    numbered.sort()
 
    for first in range(n - 2):
        val1, idx1 = numbered[first]
        left = first + 1
        right = n - 1
 
        while left < right:
            val2, idx2 = numbered[left]
            val3, idx3 = numbered[right]
            total = val1 + val2 + val3
 
            if total == target_sum:
                return f"{idx1} {idx2} {idx3}"
            elif total < target_sum:
                left += 1
            else:
                right -= 1
 
    return "-1"

n, x = map(int, input().split())
nums = list(map(int, input().split()))
print(find_three_sum(nums, n, x))