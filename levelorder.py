# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

def levelorder(self, root):
    # 
    if root is None:
        return []
    
    res = []
    queue = [root]

    while queue:
        level = []
        size = len(queue)

        for _ in range(size):
            node = queue.pop(0)
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        res.append(level)
    
    return res
