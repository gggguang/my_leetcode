from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1.extend(nums2)
        while len(nums1) > m + n:
            nums1.remove(0)
        nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6, 0]
n = 3
sol = Solution()
output = sol.merge(nums1, m, nums2, n)
