def majorityElement(nums):
        n=len(nums)//length
        a=n//3
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        print(d)
        for i,j in d.items():
            if j>a:
                l.append(i)
        return l
print(majorityElement([3,2,3]))
