class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)

# 利用 two pointer 
# 如果 s[i] 字串與 t[j] 字串相同，則比對 s 下一個
# 如果不同往 t 的下一個做檢查
# 如果 i 的結果跟 len(s) 一樣長則正確