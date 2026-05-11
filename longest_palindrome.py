# 409. Longest Palindrome
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        ans = 0
        hasOdd = False

        # 統計 a - z 個數
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        # 取出偶數的 value 可加入 palindrome
        for freq in count.values():
            if freq % 2 == 0:
                ans += freq
            else:
                ans += freq - 1
                hasOdd = True

        # odd value 可以加入當中間鍵
        if hasOdd:
            ans += 1

        return ans