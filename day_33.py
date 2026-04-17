# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 收集兩樹的 leaf
        def get_leaves(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            get_leaves(node.left, leaves)
            get_leaves(node.right, leaves)

        leaves_1 = []
        leaves_2 = []

        get_leaves(root1, leaves_1)
        get_leaves(root2, leaves_2)

        return leaves_1 == leaves_2


