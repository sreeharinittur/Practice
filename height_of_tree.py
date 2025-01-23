class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
def height(root):
    if root is None:
        return -1
    lheight=height(root.left)
    rheight=height(root.right)
    return max(lheight,rheight) + 1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(height(root))
        