# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def count_path(current_node, target_sum, current_path):
            if not current_node:
                return 0

            current_path.append(current_node.val)
            path_count = 0
            path_sum = 0

            # sum from back
            for i in range(len(current_path)-1, -1, -1):
                path_sum += current_path[i]
                if path_sum == target_sum:
                    path_count += 1

            path_count += count_path(current_node.left, target_sum, current_path)
            path_count += count_path(current_node.right, target_sum, current_path)
            current_path.pop()

            return path_count

        return count_path(root, targetSum, [])