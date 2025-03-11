class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        stack = [char for char in s if char in vowels] # 檢查 str 中有沒有母音部分有加入 stack
        result = []

        for char in s:
            if char in vowels:
                result.append(stack.pop())
            else:
                result.append(char)


        return "".join(result) 



# 利用 for 迴圈加上 stack 將含有 aeiouAEIOU 字母部分加入 stack 
# 再用 for 迴圈將有字母的部分 pop 出來做替換