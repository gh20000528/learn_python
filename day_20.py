class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 步驟 1：統計每個數字出現的次數
        freq_map = {}
        for num in arr:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1

        # 步驟 2：將出現次數收集起來
        occurrences = []
        for key in freq_map:
            occurrences.append(freq_map[key])

        # 步驟 3：檢查是否有重複次數
        seen = set()
        for count in occurrences:
            if count in seen:
                return False
            seen.add(count)

        # 步驟 4：沒有重複，回傳 True
        return True