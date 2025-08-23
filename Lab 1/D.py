def is_sorted(tests):
    for i in range(tests):
        length = int(input())
        arr = input().split(' ')
        flag = True
        for j in range(length-1):
            if int(arr[j]) <= int(arr[j+1]): 
               pass
            else: 
               flag = False; break
 
        if flag== True:
             print('YES')
        else:
             print('NO')
 
tests = int(input())
is_sorted(tests)