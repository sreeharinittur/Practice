def consecutive_duplicates(s):
    l=""
    for i in range(len(s)):
        if s[i] in l://condition
            continue
        else:
            l+=s[i]
    return l
print(consecutive_duplicates(""))
