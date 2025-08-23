def fast_sum(tests):
    for i in range(tests):
        num=int(input())
        sum= num*(num+1)/2
        print(int(sum))
 
tests= int(input())
fast_sum(tests)