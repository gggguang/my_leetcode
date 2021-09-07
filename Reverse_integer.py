class Solution:
    def reverse(self, x: int) -> int:
        min = -2 ** 31
        max = 2 ** 31 - 1 + 1  # for index
        limits = range(min, max)

        if x not in limits:
            return 0

        if "-" in str(x):
            reversed_x = reversed(str(x)[1:])
            digits = "".join(reversed_x)
            output = "-" + digits
            if int(output) not in limits:
                return 0
            else:
                return int(output)

        else:
            reversed_x = reversed(str(x))
            output = "".join(reversed_x)
            if int(output) not in limits:
                return 0
            else:
                return int(output)

sol = Solution()
output = sol.reverse(1534236469)
print(output)


# Better solution
"""
if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)
"""
