class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        def dfs(house):
            if house >= len(nums):
                return 0
            if house in mem:
                return mem[house]
            
            rob = nums[house] + dfs(house + 2)
            skip = dfs(house + 1)
            mem[house] = max(rob, skip)
            return mem[house]
        return dfs(0)