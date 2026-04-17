# 3	是數字 → 累加到 k = 3
# [	推進 stack：num_stack.push(3)，str_stack.push("")
# a	是字母 → 加入 current_str = "a"
# 2	是數字 → k = 2
# [	推進 stack：num_stack.push(2)，str_stack.push("a")
# c	是字母 → current_str = "c"
# ]	結束當前層：repeat = 2, prev = "a"，展開：current_str = "a" + "c"*2 = "acc"
# ]	結束外層：repeat = 3, prev = ""，展開：current_str = "" + "acc"*3 = "accaccacc"


class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        current_str = ''
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                num_stack.append(k)
                str_stack.append(current_str)
                current_str = ''
                k = 0
            elif char == ']':
                repeat = num_stack.pop()
                prev_str = str_stack.pop()
                current_str = prev_str + current_str * repeat
            else:
                current_str += char

        return current_str


