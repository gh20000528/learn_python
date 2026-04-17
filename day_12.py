class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0 # 紀錄最大面積

        while left < right:
            # 計算面積
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area) # 更新最大面積

            # 移動較低指標
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
        