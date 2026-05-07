# 572. Subtree of Another Tree
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a, b):
            if a is None and b is None:
                return True

            if a is None or b is None:
                return False 

            if a.val != b.val:
                return False

            return (isSameTree(a.left, b.left) and isSameTree(a.right, b.right))

        if root is None:
            return False
        
        if isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))