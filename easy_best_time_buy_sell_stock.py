class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy, profit = prices[0], 0
        for i in range(1, len(prices)):
            if buy > prices[i]: buy = prices[i]
            else: profit = max(profit, prices[i] - buy)
        return profit
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# https://youtu.be/E2-heUEnZKU?feature=shared
"""
consider first day as buy, then u decide to buy or sell from next day
start loop from second day
check if price u buyed is greater than than today's price, if yes then update buy price to that days
else choose max from previous profit and current (today's price - buying price)
repeat till last, and return maximum profit
"""