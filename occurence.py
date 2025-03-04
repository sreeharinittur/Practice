def occurence(s,c):
    if len(s)<1:
        return 0
    if s==c:
        return 1
    if s[0]==c:
        return 1+occurence(s[1:],c)
    else:
        return occurence(s[1:],c)
print(occurence("pppa","b"))