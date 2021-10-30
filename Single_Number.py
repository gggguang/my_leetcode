from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n_set = set(nums)
        for n in n_set:
            if nums.count(n) == 1:
                return n

nums = [1]
sol = Solution()
output = sol.singleNumber(nums)
print(output)
