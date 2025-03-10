class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        stack = [char for char in s if char in vowels]
        result = []

        for char in s:
            if char in vowels:
                result.append(stack.pop())
            else:
                result.append(char)


        return "".join(result) 