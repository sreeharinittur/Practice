def sumn(n):
    if int(n)<10:
        return int(n)
    return int(n[0])+sumn(n[1:])
print(sumn("87870"))
