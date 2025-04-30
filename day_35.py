# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs_from_node(node, current_sum):
            if not node:
                return 0
            count = 0
            if node.val == current_sum:
                count += 1
            count += dfs_from_node(node.left, current_sum - node.val)
            count += dfs_from_node(node.right, current_sum - node.val)
            return count


        if not root:
            return 0

        count = dfs_from_node(root, targetSum)

        count += self.pathSum(root.left, targetSum)
        count += self.pathSum(root.right, targetSum)

        return count

