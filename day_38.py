# Q1:
#將一個 有序陣列 轉換成一棵「高度平衡的 BST」。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#把 array 轉換成 balances binary tree, 所以使用 divide and conquer 中間點為 root, 然後 mid 前的 element 加 left tree, mid 後的 element 加入 right tree
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        mid = len(nums) // 2 # 用整數除法除以 2，取整數結果（不會有小數）
        root = TreeNode(nums[mid]) 
        
        root.left = self.sortedArrayToBST(nums[:mid]) # 左半邊 => 左子樹
        root.right = self.sortedArrayToBST(nums[mid+1:]) # 右半邊 => 右子樹
        
        return root





# Q2:
#應該從左到右掃描整個陣列，持續更新「目前為止見過的最低價（min_price）」與「當前價位若賣出可獲得的最大利潤」。

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)  # 嘗試賣出看有無更大利潤

        return max_profit