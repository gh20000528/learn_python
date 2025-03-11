class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []

        for i in range(len(words) -1, -1, -1): # 倒序遍歷單字
            res.append(words[i]) # 加入當前單字
            if i != 0:
                res.append(" ") # 不是最後一個單字時，加入空格

        return "".join(res)