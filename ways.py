def ways(n):
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    return ways(n-2)+ways(n-1)+ways(n-3)
print(ways(10))