class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = [] # at last do nums1 = ans
        i = 0
        j = 0
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i+=1
            else:
                ans.append(nums2[j])
                j+=1
        
        while i<m:
            ans.append(nums1[i])
            i+=1
        while j<n:
            ans.append(nums2[j])
            j+=1
        nums1[:] = ans # this makes sure that the nums1 is changed properly and references the new list instead
# https://leetcode.com/problems/merge-sorted-array/description/