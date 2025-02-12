s="M"
s3=s
s=list(s)
l=0
r=len(s)-1
def palindrome(l,r,s):
    if l>=r:
        return "".join(s)
    s[l],s[r]=s[r],s[l]
    palindrome(l+1,r-1,s)
    s2=""
    for i in s:
        s2+=i
    return s2
s1=palindrome(l,r,s)
if s3==s1:
    print("True")
else:
    print("False")
