inidef calc(coins,target)://function definition
    coins2=sorted(coins)
    res=0
    for i in range(len(coins)-1,-1,-1):
        if target>=coins2[i]:
            cnt=target//coins2[i]
            res+=cnt
            target-=cnt*coins2[i]
    return res

coins=[10,5,2,1]//array definition
target=3//target number
print(calc(coins,target))//print
