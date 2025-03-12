class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums) # 生成一個跟 nums 一樣長的 [1, 1, 1] array 

        # 紀錄 nums[i] 左邊的 item
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]


        # 紀錄 nums[i] 右邊的 item
        right = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
