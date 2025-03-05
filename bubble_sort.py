def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]//swap
    return arr
arr=[222,22,33,1,-5]//array
print(bubble_sort(arr))
