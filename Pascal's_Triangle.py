from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row in range(0, numRows):
            triangle.append([1] * (row+1))
            if row == 0 or row == 1:
                continue

            for space in range(len(triangle[row]) - 1):
                triangle[row][space+1] = sum(triangle[row-1][0+space: 2+space])
        return triangle


sol = Solution()
numRows = 5
output = sol.generate(numRows)
print(output)