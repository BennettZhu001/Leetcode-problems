# 322
"""

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""

from typing import List
from math import inf


# CoinChange problem solution:
# Five steps to do DP:
# (1) define subproblems. The subproblems in this problem are simply smaller amount with the same set of coins.
# (2) guessing. How to guess the solution? We can only choose coin from coins. There are guesses for coin in coins.
# we pick a coin and decrease amount by the value of the coin. Then check the same function with coins. Coin in coins are the guess/options.
# (3) relate problem to solutions to subproblems. We can solve problem by solving subproblems and minimize over them.
# (4) recursion and memoization, or build dp from bottom up.
# dp(i) = min_{coin} dp(i-coin) + 1 if dp(i-coin) >= 0
# (5) solve the original problem.


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        elif amount < min(coins):
            return -1

        elif amount in coins:
            return 1

        coins_small = [coin for coin in coins if coin < amount]

        curr = float("inf")

        for _ in range(len(coins_small)):
            number_coins = self.coinChange(coins_small, amount - coins_small[_])
            if number_coins != -1:
                curr = min(curr, 1 + number_coins)

        if curr == float("inf"):
            return -1
        else:
            return curr

    def coinChange_memoized(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def dp(i):
            if i in memo:
                return memo[i]
            elif i < min(coins):
                memo[i] = -1
                return -1
            elif i in coins:
                memo[i] = 1
                return 1
            else:
                coins_small = [coin for coin in coins if coin < i]

                curr = float("inf")

                for _ in range(len(coins_small)):
                    number_coins = dp(i - coins_small[_])
                    if number_coins != -1:
                        curr = min(curr, 1 + number_coins)

                if curr == float("inf"):
                    memo[i] = -1
                    return -1
                else:
                    memo[i] = curr
                    return curr

        return dp(amount)

    def coinChange_bottom_up(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        numbers = [0] * (amount + 1)

        for i in range(1, amount + 1):
            if i < min(coins):
                numbers[i] = -1
            elif i in coins:
                numbers[i] = 1
            else:
                new_i_s = [i - coin for coin in coins if coin < i]
                curr = inf
                for new_i in new_i_s:
                    if numbers[new_i] != -1:
                        curr = min(curr, 1 + numbers[new_i])

                if curr == inf:
                    numbers[i] = -1

                else:
                    numbers[i] = curr

        return numbers[amount]


def main():
    test_cases = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([2, 5], 6, 3),
        ([2, 4], 7, -1),
    ]

    solution = Solution()
    methods = [
        solution.coinChange,
        solution.coinChange_memoized,
        solution.coinChange_bottom_up,
    ]

    for method in methods:
        for coins, amount, expected in test_cases:
            actual = method(coins, amount)
            assert actual == expected, (
                f"{method.__name__}(coins={coins}, amount={amount}): "
                f"expected {expected}, got {actual}"
            )

    print("All coin change tests passed!")


if __name__ == "__main__":
    main()
