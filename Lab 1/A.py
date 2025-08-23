def odd_even(ops):
    for i in range(ops):
        n=int(input())
        if n%2==0:
            print(f"{n} is an Even number.")
        else:
            print(f"{n} is an Odd number.")
            
ops= int(input())
odd_even(ops)