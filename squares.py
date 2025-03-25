def squares(n):
    if n==1:
        return 1
    return n+squares(n-1)
print(squares(6))