class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        while True:
            temp = 0
            while n > 0:
                temp += (n%10)**2
                n = n//10
            if temp in hash_set: return False
            elif temp == 1: return True
            hash_set.add(temp)
            n = temp
# https://leetcode.com/problems/happy-number/description/
s = Solution()
print(s.isHappy(4))
# basically if we reach 1 then happy, if we see sums are repeating anywhere it is a loop and thus not happy