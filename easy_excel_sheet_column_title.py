class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            res = chr((columnNumber%26) + ord('A')) + res # take remainder
            columnNumber //= 26 # then do for quotient
        return res
# https://leetcode.com/problems/excel-sheet-column-title/
"""
https://youtu.be/q8DkXSns3Xk?feature=shared
good explanation

This logic is similar to how we convert a decimal number to it's binary form
2 | 8        -> 0 (8%2)
2 | 4 (8//2) -> 0 (4%2)
2 | 2 (4//2) -> 0 (2%2)
2 | 1 (2//2) -> 1 (1%2)
2 | 0 (1//2) -> 0 (0%2) -- loop ends

now 8 =    0           1           0           0           0
i.e.8 = (0 x 2^4) + (1 x 2^3) + (0 x 2^2) + (0 x 2^1) + (0 x 2^0)
"""