class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target - nums[-1] > 0:
            return nums.index(nums[-1]) + 1

        else:
            for num in nums:
                if target - num <= 0:
                    return nums.index(num)