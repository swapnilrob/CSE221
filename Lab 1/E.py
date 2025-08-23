def reverse_sort(len1):
    arr1= input().split(' ')
    for i in range(len1):
        flag1 = False
        for j in range(len1-2):
            if int(arr1[j]) > int(arr1[j+2]):
                arr1[j],arr1[j+2] = arr1[j+2],arr1[j]
                flag1 = True
        if flag1 == False:
            break
 
    flag2= True
    for i in range(len1-1):
        if int(arr1[i])> int(arr1[i+1]):
            flag2= False
            break
    if flag2== True:
        print('YES')
    else:
        print('NO')
 
len1=int(input())
reverse_sort(len1)