def permute(s,chosen=""):
    if len(s)==0:
        print(chosen)
        return
    for i in range(len(s)):
        ch=s[i]
        remaining=s[:i]+s[i+1:]
        permute(remaining,chosen+ch)//recursion
word="ABC"
print(permute(word))
