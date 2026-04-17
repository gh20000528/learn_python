class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == '*':
                if stack:
                    stack.pop() # 每個 * 拿掉前面一個字元
            else:
                stack.append(char) # 遇到一般字元就推進 stack

        return ''.join(stack)