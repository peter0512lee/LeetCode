# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        max_depth = -1
        def dfs(node, depth):
            nonlocal ans, max_depth
            if node is None:
                max_depth = max(max_depth, depth)
                return depth
            left_max_depth = dfs(node.left, depth + 1)
            right_max_depth = dfs(node.right, depth + 1)
            if left_max_depth == right_max_depth == max_depth:
                ans = node
            return max(left_max_depth, right_max_depth)
        dfs(root, 0)
        return ans