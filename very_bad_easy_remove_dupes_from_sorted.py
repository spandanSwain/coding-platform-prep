class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# It wants the unique values in sorted format at start of the array and also the number of unique values, catch is we only have to return the unique values length (let k), but the leetcode checks the first k elements in that array
# For input: [0,0,1,1,1,2,2,3,3,4]
# We got output: k=5 and nums was [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]