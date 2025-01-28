class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

a1=ListNode(5)
a2=ListNode(4)
a3=ListNode(3)
a1.next=a2
a2.next=a3
b1=ListNode(4)
b2=ListNode(3)
b1.next=b2
print(a1.val)
print(b1)
def process(a1,b1):
    s1=""
    s2=""
    while a1:
        s1+=str(a1.val)
        a1=a1.next
    while b1:
        s2+=str(b1.val)
        b1=b1.next
    
    i1=int(s1)
    i2=int(s2)
    i3=i1+i2
    print(i1)
    print(i2)
    print(i3)
    s3=str(i3)
    current=ListNode(int(s3[0]))
    
print(process(a1,b1))