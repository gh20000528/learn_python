# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0

            # 如果這個節點大於目前為止最大值，算是 good node
            count = 1 if node.val >= max_so_far else 0
            # 更新 max 值
            max_so_far = max(max_so_far, node.val)

            # 遞迴左子樹 + 右子樹
            count += dfs(node.left, max_so_far)
            count += dfs(node.right, max_so_far)

            return count

        return dfs(root, root.val)  # 初始最大值就是 root 自己