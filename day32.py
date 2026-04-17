# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        Hl = self.maxDepth(root.left)
        Hr = self.maxDepth(root.right)

        return max(Hl, Hr) + 1


# 先檢查 root != null
# 再檢查左樹, 右樹的高度
# return 左右樹中較高的
# 再加上 root