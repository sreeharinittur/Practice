a=[10,9,8,-50,50]
def i_sort(a):
    for i in range(1,len(a)):
        
        for j in range(i):
            if a[j]>a[i]:
                a[i],a[j]=a[j],a[i]//swapping


    return a
print(i_sort(a))
    
