class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            if (n&1) == 1: ans+=1
            n = n >> 1
        return ans
# https://leetcode.com/problems/number-of-1-bits/description/
"""
saw the logic and applied own code
"""