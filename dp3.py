def climb_stairs(n):
    if n<=2:
        return n
    return climb_stairs(n-1)+climb_stairs(n-2)//recursive call
print(climb_stairs(4))//print
