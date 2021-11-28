from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx - 1]:
                profit += (prices[idx] - prices[idx - 1])
                print(profit)
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        minprice = float("inf")
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice

        return maxprofit

if __name__ == "__main__":
    print(Solution().maxProfit2([7, 1, 5, 3, 6, 4]))
    # print(Solution().maxProfit2([7, 1, 5, 4, 3, 2, 1]))
