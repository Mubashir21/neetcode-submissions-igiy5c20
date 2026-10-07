class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        def dfs(money):
            if money == 0:
                return 0
            if money < 0:
                return float('inf')
            if money in mem:
                return mem[money]
            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(money - coin))
            mem[money] = res
            return mem[money]
        res = dfs(amount)
        return res if res != float('inf') else -1