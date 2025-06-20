import collections
class TreeNode:
    def __init__(self,val,left,right)://constructor
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def levelorder(self,root:TreeNode):
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            qlen=len(q)//length
            level=[]
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                if level:
                    res.append(level)
        return res

        
