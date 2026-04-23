# Example 1:

# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].



class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = [(score[i], i) for i in range(len(score))]
        arr.sort(reverse = True)

        res = [""] * len(score)

        for rank in range(len(arr)):
            if rank == 0:
                rank[idx] = "Gold Medal"
            elif rank == 1:
                rank[idx] = "Silver Medal"
            elif rank == 2:
                rank[idx] = "Bronze Medal"
            else:
                res[idx] = str(rank + 1)

        return res
