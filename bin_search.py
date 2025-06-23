a=[10,20,30,40]
def binary_search(start1,end1,a,ele):
    flag=0
    n=len(a)
    if n==0:
        return None
    if n==1:
        return 0
    if start1>end1:
        return -1
    mid=(start1+end1)//2
    if a[mid]==ele:#best case where mid one is the search element
        flag=1
        return mid
    elif a[mid]<ele:
        return binary_search(mid+1,end1,a,ele)
    else:
        return binary_search(start1,mid-1,a,ele)
    
print(binary_search(0,3,a,55))
