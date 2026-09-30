class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0

        for i in range(len(prices)):
            res = max(res, prices[i] - prices[l])

            if prices[i] < prices[l]:
                l = i
        return res