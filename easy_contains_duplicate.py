class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for n in nums:
            if n not in s: s.add(n)
            else: return True
        return False
# https://leetcode.com/problems/contains-duplicate/description/