class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # 如果 zero 大於視窗移動左邊界
            while zero_count > k: 
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # 計算視窗長度
            max_len = max(max_len, right - left + 1)
        
        return max_len
