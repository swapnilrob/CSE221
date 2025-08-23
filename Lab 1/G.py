def student_rank_sort(n):
    s_id = input().split(); 
    s_mark = input().split()
    total_swaps = 0
 
    for i in range(n - 1):
        change = False; top = i
        for j in range(i + 1, n):
            if int(s_mark[j]) > int(s_mark[top]):
                top = j; change = True
            elif int(s_mark[j]) == int(s_mark[top]) and int(s_id[j]) < int(s_id[top]):
                top = j; change = True
        s_id[i], s_id[top] = s_id[top], s_id[i]
        s_mark[i], s_mark[top] = s_mark[top], s_mark[i]
        if change: total_swaps += 1
 
    print(f'Minimum swaps: {total_swaps}')
    for i in range(n):
        print(f'ID: {int(s_id[i])} Mark: {int(s_mark[i])}')
student_rank_sort(int(input()))