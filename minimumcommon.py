class Minimum:
    def __init__(self):
        pass
    def minimumCommon(self,nums1,nums2):
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    return nums1[i]
        return -1
m=Minimum()
a=[1,2,3,4]
b=[3,4]
print(m.minimumCommon(a,b))