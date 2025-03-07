def qs(arr):
    if len(arr)<=1:
        return arr
    p=arr[-1]
    smaller=[]
    equal=[]
    bigger=[]
    
    for i in arr:
        if i<p:
            smaller.append(i)
        elif i>p:
            bigger.append(i)
        else:
            equal.append(i)
    return qs(smaller)+equal+ qs(bigger)
arr = [34, 7, 23, 32, 5, 62]
print(qs(arr))