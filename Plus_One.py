from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = "".join([str(i) for i in digits])
        nums = int(nums) + 1
        output = [j for j in str(nums)]
        return output


digits = [1, 2, 9]
sol = Solution()
output = sol.plusOne(digits)
print(output)