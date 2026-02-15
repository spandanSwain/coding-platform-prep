class Solution:
    def mySqrt(self, x: int) -> int:
        i, j, ans = 0, x, 0
        while i<=j:
            mid = (i+j)//2
            if mid*mid > x:
                j = mid-1
            else:
                i = mid+1
                ans = mid
        return ans
# DONT'T USE BUILT-IN FUNCTION
# https://leetcode.com/problems/sqrtx/