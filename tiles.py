def tiles(n):
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    return tiles(n-1)+tiles(n-2)
print(tiles(6))