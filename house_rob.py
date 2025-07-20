def house_rob(arr):
    if len(arr)==1:
        return arr[0]
    if len(arr)==2:
        return max(arr)
    return max(arr[-1]+house_rob(arr[:-2]),house_rob(arr[:-1]))//recursion
print( house_rob([5]))
