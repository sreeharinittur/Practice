import collections
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
t=TreeNode(5)
t1=TreeNode(4)
t2=TreeNode(15)
t3=TreeNode(20)
t.left=t1
t.right=t2
t2.right=t3
def display(t):
    res=[]
    if not t:
        return res
    q=collections.deque()
    q.append(t)   
    while q:
        sl=[]
        for _ in range(len(q)):
            node=q.popleft()
            sl.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(sl)
    return res
print(display(t))