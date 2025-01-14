def pow2(n):
    i=2
    flag=0
    if n==2:
        return True
    if n==1:
        return True
    if n==0:
        return False
    while i!=n:
        i=i*2
        if i==n:
            flag=1
            break
        if i>n:
            break
    if flag==0:
        return False
    else:
        return True
print(pow2(8))
print(pow2(10))