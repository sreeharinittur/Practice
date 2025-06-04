
def alien_language(n):
    s=""
    if n==1:
        s+="C"
    if n%2==0:
        s=s+"A"+alien_language(n/2)//function calling itself
        #s+alien_language(n/2)
    if n>1 and n%2!=0:
        s=s+"B"+alien_language(n-1)//function calling
        
    return s
print(alien_language(6))//output
