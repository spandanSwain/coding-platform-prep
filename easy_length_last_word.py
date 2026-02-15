class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        test_split = s.split(' ') # we can also do normal s.split() instead of adding ' '
        new_split = []
        for word in test_split:
            if word != '': new_split.append(word)
        # return len(new_split[-1])
        # OR
        # return len(s.split()[-1])
    
# https://leetcode.com/problems/length-of-last-word/submissions/1759385592/