class Q:
    def __init__(self):
        self.s1=[]
    def push(self,x):
        self.s1.append(x)
    def pop(self):
        a=self.s1[0]
        self.s1.remove(self.s1[0])
        return a
    def peek(self):
        return self.s1[0]
    def is_empty(self):
        if len(self.s1)==0:
            return True
        else:
            return False
    def display(self):
        print(self.s1)
sobj=Q()
sobj.push(5)
sobj.push(6)
sobj.push(7)
sobj.display()
print(sobj.peek())
sobj.pop()
print(sobj.peek())
sobj.display()
