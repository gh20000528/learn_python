# Python 的 set 有內建支援差集（difference）與交集（intersection）操作！
# set 的底層為 hash
# 差集：在 set1 但不在 set2
# 差集：在 set2 但不在 set1
# nums1 = [1, 2, 3]
# nums2 = [2, 4, 6]
# set1 = {1, 2, 3}
# set2 = {2, 4, 6}
# set1 - set2 = {1, 3}
# set2 - set1 = {4, 6}

# ➜ return [[1, 3], [4, 6]]


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        only_in_nums1 = list(set1 - set2)
        only_in_nums2 = list(set2 - set1)

        return [only_in_nums1, only_in_nums2]


