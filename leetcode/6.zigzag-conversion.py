#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
# @lc code=end
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            
            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False
            
            current_row += 1 if going_down else -1
        
        return ''.join(rows)