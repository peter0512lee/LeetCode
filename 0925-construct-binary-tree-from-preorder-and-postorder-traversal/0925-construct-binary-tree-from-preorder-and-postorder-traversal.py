# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        # find the root 
        root = TreeNode(postorder.pop())
        if len(preorder) == 1:
            return root
        # find the right index
        right_idx = preorder.index(postorder[-1])
        # construct
        root.right = self.constructFromPrePost(preorder[right_idx:], postorder)
        root.left = self.constructFromPrePost(preorder[1:right_idx], postorder)

        return root
