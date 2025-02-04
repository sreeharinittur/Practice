s=input()
def highestFrequencyCharacter(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    maxi=max(d.values())

    for i,j in d.items():
        if j==maxi:
            return i
print(highestFrequencyCharacter(s))
