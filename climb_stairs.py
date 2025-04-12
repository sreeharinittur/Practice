def climb_stairs(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==0:
        return 1
    return climb_stairs(n-1)+climb_stairs(n-2)//recursive call
    
print(climb_stairs(4))
