def occur(string,c):
    if len(string)<1:
        return ""
    if string[0]==c:
        return occur(string[1:],c)
    else:
        return string[0]+occur(string[1:],c)//recursion


   
print(occur("iii","i"))
