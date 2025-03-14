class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 建立無窮大的值
        first = float('inf') 
        second = float('inf')

        for num in nums:
            # 找到第一小的
            if num <= first:
                first = num
            # 第二小的
            elif num <= second:
                second = num
            else:
                return True

        return False
            
