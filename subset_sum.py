def subset(nums,target,index=0,current=[]):
    if sum(current)==target:
        print(current)
        return
    if index>=len(nums) or sum(current)>target:
        return
    subset(nums,target,index+1,current+[nums[index]])
    subset(nums,target,index+1,current)
nums=[2,3,7,1]
target=3
print(subset(nums,target))