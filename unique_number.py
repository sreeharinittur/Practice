def unique(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i,j in d.items():
        if j==1:
            return i
    return 0
a=[8,8,8,7,0]
print(unique(a))