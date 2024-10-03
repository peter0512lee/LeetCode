# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # Important section
        if root.right is None:
            return self.minDepth(root.left) + 1
        if root.left is None:
            return self.minDepth(root.right) + 1
        
        l_depth = self.minDepth(root.left)
        r_depth = self.minDepth(root.right)

        return min(l_depth, r_depth) + 1