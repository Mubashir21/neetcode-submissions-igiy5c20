class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                res = max(prices[r] - prices[l], res)
            
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        return res