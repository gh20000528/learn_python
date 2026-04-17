class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)

        return result


# 先取得最多糖果數的人
# 在用 for 迴圈一一加上 extraCandies 確認是否是最大的