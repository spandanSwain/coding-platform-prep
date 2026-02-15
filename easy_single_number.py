class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result
# https://leetcode.com/problems/single-number/solutions/6928847/video-xor-solution//
"""
for list = [2,1,2,3,1]
0 ^ 2 ^ 1 ^ 2 ^ 3 ^ 1
= 0 ^ (2 ^ 2) ^ (1 ^ 1) ^ 3    ← Commutative & Associative
= 0 ^ 0 ^ 0 ^ 3                ← Same numbers = 0
= 3                            ← Number with 0 = itself
"""