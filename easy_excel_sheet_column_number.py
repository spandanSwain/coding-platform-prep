class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        s = columnTitle
        n = len(s)
        for i in range(n):
            ans += (ord(s[n-1-i]) - ord("A") + 1) * (26**i)
        return ans
# https://leetcode.com/problems/excel-sheet-column-number/description/
"""
to convert hexadecimal to binary this logic is used
1A = (1 x 16^1) + (A i.e. 10 x 16^0)
"""