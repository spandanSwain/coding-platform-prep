class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry, ans = 0, []

        while i>=0 or j>=0 or carry:
            total = carry
            if i>=0:
                total += int(a[i])
                i-=1
            if j>=0:
                total += int(b[j])
                j-=1
            ans.append(str(total%2)) # for total = 2 means it was 1+1 it will append 0
            carry = total // 2 # again if 1+1, then move the 1 as carry
        return "".join(reversed(ans))
# https://leetcode.com/problems/add-binary/
c = Solution()
res = c.addBinary("11", "11")
print(res)