class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        curProf = 0

        while r < len(prices):
            curProf = max(curProf, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l = r
            r += 1
        return curProf