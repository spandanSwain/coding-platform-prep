class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return not n&(n-1)
# https://leetcode.com/problems/power-of-two/description/
"""
Every power of 2 like 1,2,4,6,8,16 have only one '1' in it's binary form.
So, to see if it has only 1, we can do AND, as 1&1 = 1 and 0&1=0 0&0=0 1&0=0
if u observe, or if u byheart and check, n & (n-1) returns 0 if n is a power of 2.

Example:
    n = 8, ans is True
    n - 1 = 7
    n_2 = 1000
    n-1_2 = 0111
      
      1 0 0 0
    & 0 1 1 1
    __________
       0 0 0 0
"""