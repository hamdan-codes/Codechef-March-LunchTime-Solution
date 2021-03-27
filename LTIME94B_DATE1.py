#Author : Chaudhary Hamdan

for _ in range(int(input())):
    
    a, y, x = [int(x) for x in input().split()]
    
    if a >= y:
        print(x*y)
    else:
        print( x*a +1)
    
    
    



