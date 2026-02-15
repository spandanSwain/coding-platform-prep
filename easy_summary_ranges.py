class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums: return []
        start = nums[0]
        temp = start
        res = []
        for i in range(1, len(nums)):
            if temp+1 != nums[i]:
                if start == temp: res.append(f"{start}")
                else:
                    res.append(f"{start}->{nums[i-1]}")
                start, temp = nums[i], nums[i]
            else: temp = nums[i]
        if start == temp: res.append(f"{start}")
        else: res.append(f"{start}->{temp}")
        return res
# https://leetcode.com/problems/summary-ranges/description/