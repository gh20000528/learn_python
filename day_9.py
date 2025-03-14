class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0 # 追蹤寫入位置
        read = 0 # 讀取位置

        while read < len(chars):
            char= chars[read] # 當前字母
            count = 0 # 計數

            while read < len(chars) and chars[read] == char:
                count += 1
                read += 1 # 移動讀取指標

            # 將字母寫入壓縮後的陣列
            chars[write] = char
            write += 1 # 移動寫入指標

            # `count > 1` 將數字拆開寫入
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


            
        