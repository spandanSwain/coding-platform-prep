class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        if len(s)%2 != 0:
            return False
        else:
            for i in range(len(s)):
                if s[i] in ["(", "[", "{"]:
                    stack.append(s[i])
                else:
                    if not stack or stack[-1] != pairs[s[i]]:
                        return False
                    stack.pop()
            if stack == []:
                return True
            else:
                return False
# https://leetcode.com/problems/valid-parentheses/