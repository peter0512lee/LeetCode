# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node = {}
        children = set()
        for parent, child, is_left in descriptions:
            children.add(child)
            if parent not in node:
                node[parent] = TreeNode(parent)
            if child not in node:
                node[child] = TreeNode(child)

            # determine left or right
            if is_left:
                node[parent].left = node[child]
            else:
                node[parent].right = node[child]
            
        for p, c, l in descriptions:
            if p not in children:
                return node[p]