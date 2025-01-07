# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        # Check if the left child is a leaf
        left_sum = 0
        if root.left and not root.left.left and not root.left.right:
            left_sum = root.left.val

        # Recursively calculate for left and right subtrees
        return left_sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Instantiate the solution class and call the method
solution = Solution()
result = solution.sumOfLeftLeaves(root)

# Output the result
print(result)  # Output: 24 (9 + 15)
