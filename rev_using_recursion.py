def reverse(l,n,arr):
    if l>=n:
        return
    arr[l],arr[n]=arr[n],arr[l]
    reverse(l+1,n-1,arr)
    return arr
arr=[1,2,3,4]
print(reverse(0,3,arr))
