class Solution:
    def plusOne(self, digits):
        if not digits: return [1]
        ans, carry = [], 0

        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
# https://leetcode.com/problems/plus-one/description/
c = Solution()
print(c.plusOne([1,9,9]))