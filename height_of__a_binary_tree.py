class Tree:
    def __init__(self,root):
        self.data=root
        self.left=None
        self.right=None
def height(root):
    if root is None:
        return -1
    l=height(root.left)//recursion
    r=height(root.right)
    return 1+max(l,r)
r=Tree(5)//Initialization
r2=Tree(4)
r3=Tree(6)//initialization
r4=Tree(7)
r5=Tree(8)
r.left=r2
r.right=r3
r3.right=r4
r4.right=r5
print(height(r))
    

        
