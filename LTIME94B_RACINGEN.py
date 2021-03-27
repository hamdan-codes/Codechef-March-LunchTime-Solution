# Author: Chaudhary Hamdan

for _ in range(int(input())):
    x, r, m = [int(x) for x in input().split()]
    
    if x >= (r*60):
        if r <= m:
            print('YES')
        else:
            print('NO')
    else:
        if (x+2*(60*r-x)) <= (60*m):
            print('YES')
        else:
            print('NO')
    
    
