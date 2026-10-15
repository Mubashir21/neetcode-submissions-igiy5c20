class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def dfs(amount):
            if amount <= 0:
                return 0
            if amount in mem:
                return mem[amount]
            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            mem[amount] = res
            return mem[amount]
        res = dfs(amount)
        return res if dfs(amount) != float('inf') else -1