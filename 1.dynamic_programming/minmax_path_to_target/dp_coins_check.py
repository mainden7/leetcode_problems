import sys
from typing import List


class Solution:
    def calc(self, coin, amount):
        k = amount // coin
        u = amount % coin
        return k, u

    def get_coin(self, coins, amount):
        coins = sorted(filter(lambda x: x <= amount, coins), reverse=True)
        if not coins:
            return -1

        if len(coins) == 1:
            k, u = self.calc(coins[0], amount)
            if u == 0:
                return k
            else:
                return -1

        i = 0
        j = 0
        sr = None
        while True:
            if i >= len(coins):
                return -1

            k, _ = self.calc(coins[i], amount)
            k -= j
            if k == 0:
                i += 1
                j = 0
                continue

            u = amount - (coins[i] * k)
            if u == 0:
                return k
            if u in coins:
                return k + 1
            y = self.get_coin(coins, u)
            if y == -1:
                j += 1
                continue
            return y + k

    def rec_coin_change(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        res = float("inf")
        sub_res = self.get_coin(coins, amount)
        if sub_res:
            res = sub_res
        # def search(coin_index=0, count=0, remaining=amount):
        #     fits = remaining // coins[coin_index]
        #     ## later calls of function will have lower denominations,
        #     # so number of total coins will be more than earlier calculated coins
        #     # stored in self.min_coins, ignore
        #     if (
        #         count + fits + (remaining % coins[coin_index] != 0)
        #         >= self.min_coins
        #     ):
        #         # print("AAA", self.min_coins)
        #         return
        #
        #     if remaining % coins[coin_index] == 0:
        #         self.min_coins = min(self.min_coins, count + fits)
        #         # print("BBB", self.min_coins)
        #         return
        #
        #     if coin_index == len(coins) - 1:
        #         # print("CCC", self.min_coins)
        #         return
        #
        #     for i in range(fits, -1, -1):
        #         # count_index is next index, possible number of coins
        #         # already computed and processed, if old count of coins
        #         # is i + count , then remaining balance of amount
        #         # print("i::", i, "coin_index+1::", coin_index+1)
        #         search(
        #             coin_index + 1,
        #             i + count,
        #             remaining - i * coins[coin_index],
        #         )
        #
        # search()
        return res if res != float("inf") else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [float("inf")] * (amount + 1)
        table[0] = 0

        for x in range(min(coins), amount + 1):
            for c in coins:
                if x - c < 0:
                    continue
                table[x] = min(table[x - c] + 1, table[x])
        return table[amount] if table[amount] != float("inf") else -1


if __name__ == "__main__":
    # aa = Solution().coinChange([186, 419, 83, 408], 6249)
    bb = Solution().rec_coin_change([186, 419, 83, 408], 6249)
    # aa = Solution().coinChange([186, 419, 83, 408], 6249)
    # bb = Solution().rec_coin_change([1, 3, 5], 14)
    # bb = Solution().rec_coin_change([9, 14, 17, 23], 100)
    # cc = Solution().minCoins([1,  5], 3, 14)
    # print(aa)
    print(bb)
    # print(cc)
