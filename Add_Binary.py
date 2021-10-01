class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        output = a + b
        return bin(output)[2:]


a = "1010"
b = "1011"
sol = Solution()
output = sol.addBinary(a, b)
print(output)