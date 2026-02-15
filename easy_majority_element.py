class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count, ans = 0, 0
        for n in nums:
            if count == 0: ans = n
            count = count + 1 if ans == n else count - 1
        return ans
# https://leetcode.com/problems/majority-element/description/
# This is called BOYER-MOORE algorithm, it will work if we know there is atleast one repeating element