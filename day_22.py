class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: 用 tuple 表示每一列，放進字典裡統計出現次數
        row_map = Counter(tuple(row) for row in grid)

        # Step 2: 遍歷每一欄，轉成 tuple，看看 row_map 裡有沒有出現
        count = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += row_map.get(col, 0)

        return count



# 在 Python 中，tuple 是一種有序、不可變（immutable） 的序列資料型態。