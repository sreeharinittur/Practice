
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answers=[]
        l=nums//nums
        
        for i in range(len(l)):#for loop
            prod=1
            l2=[]
            for j in l[:i]:
                l2.append(j)
            for k in l[i+1:]://slicing
                l2.append(k)
            
            for k1 in l2:
                prod*=k1
            answers.append(prod)
        return answers
a=Solution()
print(a.productExceptSelf([-1,1,0,-3,3]))
                
            
