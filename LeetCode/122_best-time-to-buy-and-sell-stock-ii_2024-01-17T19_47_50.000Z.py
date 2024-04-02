# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MAX_PRICE = 10000
        last = None
        maxProfit = 0
        for p in prices:
            if last != None and p > last:
                maxProfit += p - last
            last = p
        return maxProfit
