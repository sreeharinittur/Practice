def subseq(index,ds,arr,summ,target):
    if index==len(arr):
        if summ==target:
            print(ds)
        return
    ds.append(arr[index])
    summ+=arr[index]
    subseq(index+1,ds,arr,summ,target)
    ds.remove(arr[index])
    summ-=arr[index]
    subseq(index+1,ds,arr,summ,target)
ds=[]
arr=[3,1,2,1]
summ=0
target=3
subseq(0,ds,arr,summ,target)
    