def find_pairs(projectCosts,target):
    a=set(projectCosts)
    count=0
    for i in projectCosts:
        if (i+target) in a:
            count+=1
    return count
#print(find_pairs([1,3,5],2))
print(find_pairs([2, 4, 6, 8, 10], 2))


