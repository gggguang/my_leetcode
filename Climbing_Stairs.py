class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        res = [1, 2]
        for i in range(n - 2):
            res.append(res[-1] + res[-2])
            print(res)
        return res[-1]

n = 8
output = Solution().climbStairs(n)
print(output)