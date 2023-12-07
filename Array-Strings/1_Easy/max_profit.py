class Solution:
    def maxProfit(self, prices: [int]) -> int:
        # sliding window
        left = 0
        max_profit = 0
        for right in range(len(prices)):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                left = right
        return max_profit

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))