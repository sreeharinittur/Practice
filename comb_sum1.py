def find_comb(ind,arr,target,ans,ds):
    if ind==len(arr):
        if target==0:
            ans.append(list(ds))//append
        return
    if arr[ind]<=target:
        ds.append(arr[ind])
        find_comb(ind,arr,target-arr[ind],ans,ds)
        ds.pop()#pop element from the ds
    find_comb(ind+1,arr,target,ans,ds)
ind=0
arr=[2,3,6,7]//array
target=7
ans=[]
ds=[]
find_comb(ind,arr,target,ans,ds)
print(ans)

