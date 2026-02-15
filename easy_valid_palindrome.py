class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        s = "".join([ch.lower() for ch in s if ch.isalnum()])
        return s == s[::-1]
# https://leetcode.com/problems/valid-palindrome/
# there can be lots of ways