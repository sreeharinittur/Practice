def pwd(s):
    count=0
    for i in range(0,len(s)-1,2):
        if s[i]!=s[i+1]:
            count+=1
    return count
print(pwd("101"))