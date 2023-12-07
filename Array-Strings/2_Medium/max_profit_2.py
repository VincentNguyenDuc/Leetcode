class Solution:
    def maxProfit(self, prices: [int]) -> int:

        length = len(prices) + 1

        # Memoization
        holds_memo = [None for _ in range(length)]
        not_holds_memo = [None for _ in range(length)]

        holds_memo[0] = -float('inf')
        not_holds_memo[0] = 0

        for i in range(1, length):
            current_price = prices[i - 1]

            # either keep hold, or buy in stock today at stock price
            holds_memo[i] = max(
                holds_memo[i - 1],
                not_holds_memo[i - 1] - current_price
            )

            # either keep not-hold, or sell out stock today at stock price
            not_holds_memo[i] = max(
                not_holds_memo[i - 1],
                holds_memo[i - 1] + current_price
            )

        # maximum profit must be in not-hold state
        return not_holds_memo[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([1, 2, 3, 4, 5]))
