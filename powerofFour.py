class POT:
    def __init__(self):
        pass
    def pot(self,n):
        if n==4 or n==1:
            return True
        elif n<4 and n!=1:
            return False
        return (n%4)==0 and self.pot(n/4)
p=POT()
print(p.pot(1))