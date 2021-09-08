x = 10
x = str(x)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return True
        else:
            return False


# Better solution
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])
"""
