class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0

        for i ,num in enumerate(nums):
            if leftsum == (total - num - leftsum):
                return i
            leftsum += 1
        
        return -1
