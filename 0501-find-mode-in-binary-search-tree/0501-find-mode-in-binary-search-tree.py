# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def inorder(root):
            if not root:
                return 
            lst.append(root.val)
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        freq = Counter(lst)
        max_freq = max(freq.values())

        return [x for x in freq if freq[x] == max_freq]