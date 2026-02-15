class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sd, td, i = {}, {}, 0
        
        while i < len(s):
            if s[i] not in sd: sd[s[i]] = t[i]
            elif s[i] in sd and sd[s[i]] != t[i]: return False
            if t[i] not in td: td[t[i]] = s[i]
            elif t[i] in td and td[t[i]] != s[i]: return False
            i+=1
        return True
# https://leetcode.com/problems/isomorphic-strings/description/