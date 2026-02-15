# FIRST APPROACH (OWN TRY) -- SLOWEST SOLUTION BUT CORRECT LOGICALLY
def reverseBits(self, n: int) -> int:
    s = self.convertToBinary(n)
    return self.convertToDecimal(s)

def convertToBinary(self, n: int) -> str:
    res = ""
    while n > 0:
        res = str(n%2) + res
        n //= 2
    res = res.zfill(32)
    return res

def convertToDecimal(self, s: str) -> int:
    ans = 0
    for i in range(32):
        ans += int(s[i]) * (2**i)
    return ans
# https://leetcode.com/problems/reverse-bits/
"""
The bitwise approach is just: logic for second approach

Initialize ans = 0.
Take LSB of n → (n & 1).
Shift ans left by 1 to make space. (do left shift of 1)
Insert the LSB into ans → (ans << 1) | (n & 1). (first barcket shifts to left, second bracket assigns value)
Shift n right by 1 to drop the bit we just used. (update the number by ignoring the LSB, i.e right shift by 1)
Repeat 32 times (since we're dealing with 32-bit integers). (repeat 32 times, int is 32 bit)
"""
# SECOND APPROACH 
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) | (n & 1)
            n = n >> 1
        return ans