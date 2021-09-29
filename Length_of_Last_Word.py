class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


s = "Hello World    "
sol = Solution()
output = sol.lengthOfLastWord(s)
print(output)