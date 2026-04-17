class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: 長度不同一定不行
        if len(word1) != len(word2):
            return False

        # Step 2: 紀錄每個字母出現次數
        freq1 = {}
        freq2 = {}

        for ch in word1:
            freq1[ch] = freq1.get(ch, 0) + 1
        for ch in word2:
            freq2[ch] = freq2.get(ch, 0) + 1

        # Step 3: 比較字母集合
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        # Step 4: 比較頻率集合
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True