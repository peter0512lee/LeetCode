# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None
        val_lst = []
        def dfs(node):
            if not node: return None
            val_lst.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        val_lst.sort()
        return val_lst[k-1]