class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s if i.isalnum()]
        s = "".join(s).lower()
        if s == s[::-1]:
            return True
        else:
            return False


s = "A man, a plan, a canal: Panama"
# s = "0P"
sol = Solution()
output = sol.isPalindrome(s)
print(output)