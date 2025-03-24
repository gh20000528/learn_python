class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 取 nums 前 k 個值的 sum
        wSum = sum(nums[:k])
        # 總和平均值
        mSum = wSum / k

        # for 回圈找出最大平均值
        for i in range(k, len(nums)):
            wSum = wSum - nums[i - k] + nums[i]
            mSum = max(wSum / k, mSum)

        return mSum