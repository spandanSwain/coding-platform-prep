class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans = [[1], [1,1]]
        if rowIndex == 0 or rowIndex == 1: return ans[rowIndex]
        n = rowIndex
        while n > 0:
            ref = ans[-1]
            temp = [1]
            for i in range(0, len(ref)-1):
                temp.append(ref[i] + ref[i+1])
            temp.append(1)
            ans.append(temp)
            n -= 1
        return ans[rowIndex]
# https://leetcode.com/problems/pascals-triangle-ii/description/