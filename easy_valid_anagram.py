class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        d,s,t = {}, s.upper(), t.upper()
        for i in s: d[ord(i)-ord("A")] = d.get(ord(i)-ord("A"), 0) + 1
        for j in t: d[ord(j)-ord("A")] = d.get(ord(j)-ord("A"), 0) - 1
        for k,v in d.items():
            if v!=0: return False
        return True
# https://leetcode.com/problems/valid-anagram/description/