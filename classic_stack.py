class valid:
    def is_valid(self,s):
        stack=[]
        for i in s:
            if i=="(":
                stack.append(i)//append
            elif i==")":
                if stack and stack[-1]=="(":
                    stack.pop()//remove
                else:
                    return False
            else:
                continue
        if len(stack)==0:
            return True
        else:
            return False
v=valid()
s="(PQR))"
print(v.is_valid(s))
