class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        maps = {}

        def dfs(money):
            if money in maps:
                return maps[money]
            if money == amount:
                return 0
            if money > amount:
                return float("inf")


            ways = float("inf")
            for coin in coins:
                ways = min(ways, 1 + dfs(money + coin))
            
            maps[money] = ways
            return ways

        res = dfs(0)
        return res if res != float("inf") else -1