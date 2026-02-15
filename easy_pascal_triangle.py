class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1], [1,1]]
        if numRows==1 or numRows==2: return ans[0:numRows]
        for _ in range(numRows-2):
            ref = ans[-1]
            temp = [1]

            for i in range(0, len(ref)-1):
                temp.append(ref[i] + ref[i+1])
            temp.append(1)
            ans.append(temp)
        return ans
# https://leetcode.com/problems/pascals-triangle/