class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        s = 0
        while num >= 10:
            num = self.helper(num)
        return num

    def helper(self, tmp: int) -> int:
        s = 0
        while tmp>0:
            s += tmp%10
            tmp//=10
        return s
# https://leetcode.com/problems/add-digits/