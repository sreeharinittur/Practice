def rotate( nums, k):
    k=k%len(nums)
    nums2=[0]*len(nums)
    for i in range(len(nums)):
        a=(i+k)%len(nums)
        nums2[a]=nums[i]
    for i in range(len(nums)):
        nums[i]=nums2[i]
    return nums
a=[1,2]
k=3
print(rotate(a,k))