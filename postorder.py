class Node:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
class Solution:
    def postorder(self,root):
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val,end=" ")
if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.right.right=Node(4)
    s=Solution()
    s.postorder(root)
