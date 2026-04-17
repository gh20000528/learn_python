class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alitude = [0]
        for g in gain:
            alitude.append(alitude[-1] + g)

        return max(alitude)