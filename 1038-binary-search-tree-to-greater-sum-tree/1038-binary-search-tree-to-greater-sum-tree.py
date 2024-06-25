# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0
        def dfs(n):
            if n:
                dfs(n.right)
                self.total +=  n.val
                n.val       =  self.total
                dfs(n.left)
        dfs(root)
        return root