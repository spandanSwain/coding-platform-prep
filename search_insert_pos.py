class Solution:
    def searchInsert(self, nums, target: int) -> int:
        idx = 0
        """
        we can comment this
        while idx != len(nums):
            if nums[idx] == target: return idx
            idx+=1
        """
        left = 0
        right = len(nums)

        while left < right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid+1
        return left
# https://leetcode.com/problems/search-insert-position/description/