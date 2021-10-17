from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 1e4
        for sell in prices:
            if sell - buy > 0:
                subtract = sell - buy
                if subtract > profit:
                    profit = subtract
            else:
                buy = sell
        return profit


# prices = [2, 4, 1]
prices = [7, 1, 5, 3, 6, 4]
sol = Solution()
output = sol.maxProfit(prices)
print(output)
