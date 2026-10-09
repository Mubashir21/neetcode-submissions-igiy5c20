class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def dfs(money):
            if money == amount:
                return 0
            if money in mem:
                return mem[money]
            res = float('inf')
            for coin in coins:
                if money + coin <= amount:
                    res = min(res, 1 + dfs(money + coin))
            mem[money] = res
            return mem[money]

        res = dfs(0)
        return res if res != float('inf') else -1