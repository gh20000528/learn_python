# 589. N-ary Tree Preorder Traversal
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]
# DFS


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfs(node):
            if node is None:
                return 
            ans.append(node.val)

            for child in node.children:
                # 有 child 先加進 ans
                dfs(child)
            
        dfs(root)

        return ans