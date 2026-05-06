# 563. Binary Tree Tilt
# Input: root = [1,2,3]
# Output: 1
# Explanation: 
# Tilt of node 2 : |0-0| = 0 (no children)
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
# Sum of every tilt : 0 + 0 + 1 = 1

## Tilt = | left subtree sum - right subtree sum|

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilts = 0

        def dfs(node):  
            # 這邊的 DFS 是計算左右子樹的 sum
            if node is None:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            self.total_tilts += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum

        dfs(root)

        return self.total_tilts