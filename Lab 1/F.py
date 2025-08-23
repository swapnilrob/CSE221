def ancient_sort(n):
    arr = input().split()
    for i in range(n):
        did_swap = False
        for j in range(n - 1):
            x, y = int(arr[j]), int(arr[j + 1])
            if (x % 2 == y % 2) and x > y:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = True
        if did_swap == False:
            break
    for num in arr:
        print(int(num), end=' ')
        
ancient_sort(int(input()))