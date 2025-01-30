def sum(l):
    if len(l)==1:
        return l[0]
    else:
        return l[0]+sum(l[1:])
l=[10,20,30]
print(sum(l))