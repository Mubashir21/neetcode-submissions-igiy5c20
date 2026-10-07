class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(house, end, mem):
            if house >= end:
                return 0
            if house in mem:
                return mem[house]
            rob = nums[house] + dfs(house + 2, end, mem)
            take = dfs(house + 1, end, mem)
            mem[house] = max(rob, take)
            return mem[house]
        return max(dfs(0, len(nums) - 1, {}), dfs(1, len(nums), {}))