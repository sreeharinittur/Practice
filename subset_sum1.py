def subset_sum(ind,arr,ds,s=0):
    if ind>len(arr)-1:
        ds.append(s)
        return 
    subset_sum(ind+1,arr,ds,s+arr[ind])
    subset_sum(ind+1,arr,ds,s)
ind=0
arr=[3,1,2]
ds=[]
s=0
subset_sum(ind,arr,ds,s)
print(ds)