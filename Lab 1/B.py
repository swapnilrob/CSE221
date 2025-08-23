def solve_aithmetics(tests):
    for i in range(tests):
        ops= input().split()
        val1=int(ops[1])
        oper=ops[2]
        val2=int(ops[3])
        if oper =='+':
            print(round(val1+val2, 6))
        elif oper =='-':
            print(round(val1-val2, 6))
        elif oper =='*':
            print(round(val1*val2, 6))
        elif oper =='/':
            print(round(val1/val2, 6))
        
tests=int(input())
solve_aithmetics(tests)