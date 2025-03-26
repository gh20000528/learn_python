class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # 如果視窗中超過一個 0，就要縮小視窗
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # 計算合法視窗長度，**刪除一個元素**
            max_len = max(max_len, right - left)

        return max_len
