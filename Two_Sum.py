nums = [3, 2, 4]
target = 6

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for index, num in enumerate(nums):
            if target - num in nums and target - num != num:
                output.append(index)
            elif nums.count(target - num) >= 2:
                output.append(index)
        return output


# Better solution
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        
        for i, num in enumerate(nums):
            diff = target-num
            if diff in hashmap:
                return hashmap[diff], i
            hashmap.update({num:i})
"""