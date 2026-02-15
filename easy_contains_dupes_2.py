class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
                continue
            elif nums[i] in d:
                if abs(i-d[nums[i]]) <= k: return True
                d[nums[i]] = i
        return False
# https://leetcode.com/problems/contains-duplicate-ii/