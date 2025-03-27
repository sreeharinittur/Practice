def comb_sum(ind,arr,target,ans,ds):
    if ind==len(arr):
        if target==0:
            ans.append(list(ds))
        return
    if arr[ind]<=target:
        ds.append(arr[ind])
        comb_sum(ind+1,arr,target-arr[ind],ans,ds)//call again
        ds.pop()
    comb_sum(ind+1,arr,target,ans,ds)
arr=[1,1,1,2,2]
target=4
ans=[]
ds=[]
ind=0
comb_sum(ind,arr,target,ans,ds)
print(ans)
ans2=[]
for i in ans:
    if i not in ans2:
        ans2.append(i)
    else:
        continue
print(ans2)//answer
