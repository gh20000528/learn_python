# 257. Binary Tree Paths

# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        queue = [(root, str(root.val))]
        ans = []

        while queue:
            node, path = queue.pop(0)

            if not node.left and not node.right:
                ans.append(path)
            if node.left:
                queue.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + "->" + str(node.right.val)))

        return ans
