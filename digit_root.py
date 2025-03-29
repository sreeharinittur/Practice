def digit_root(n):
    if len(n)==1:
        return n
    summ=0
    for i in n:
        summ+=int(i)
    return digit_root(str(summ))
print(digit_root("6"))