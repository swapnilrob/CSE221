def find_first_not_less_than(arr, val):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid
    return left
 
def find_first_greater_than(arr, val):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= val:
            left = mid + 1
        else:
            right = mid
    return left
 
n, q = map(int, input().split())
data = list(map(int, input().split()))
 
for _ in range(q):
    x, y = map(int, input().split())
    start = find_first_not_less_than(data, x)
    end = find_first_greater_than(data, y)
    print(end - start)