# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.


# An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # init ugly number
        ugly = [1]
        i2 = i3 = i5 = 0
        
        #  產生下一個 ugly number
        for i in range(n - 1):
            next_ugly = min(
                ugly[i2] * 2,
                ugly[i3] * 3,
                ugly[i5] * 5
            )
            
            ugly.append(next_ugly)

            if next_ugly == ugly[i2] * 2:
                i2 += 1
            if next_ugly == ugly[i3] * 3:
                i3 += 1
            if next_ugly == ugly[i5] * 5:
                i5 += 1

        return ugly[-1]    
        

