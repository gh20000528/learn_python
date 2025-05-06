#將一個 有序陣列 轉換成一棵「高度平衡的 BST」。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        mid = len(nums) // 2 # 用整數除法除以 2，取整數結果（不會有小數）
        root = TreeNode(nums[mid]) 
        
        root.left = self.sortedArrayToBST(nums[:mid]) # 左半邊 => 左子樹
        root.right = self.sortedArrayToBST(nums[mid+1:]) # 右半邊 => 右子樹
        
        return root