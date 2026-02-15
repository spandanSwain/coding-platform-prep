class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs == []: return ""
        common = ""

        for idx in range(len(strs[0])):
            char = strs[0][idx]
            if len(strs) >= 1:
                for other_str in range(1, len(strs)):
                    if idx >= len(strs[other_str]) or strs[other_str][idx] != char:
                        return common
                common += char
        return common
# https://leetcode.com/problems/longest-common-prefix/
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))