from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
        return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
output = sol.maxSubArray(nums)
print(output)
