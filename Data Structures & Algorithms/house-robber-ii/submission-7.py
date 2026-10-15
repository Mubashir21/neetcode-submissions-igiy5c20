class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dfs(start, end, mem):
            if start >= end:
                return 0
            if start in mem:
                return mem[start]
            rob = nums[start] + dfs(start + 2, end, mem)
            skip = dfs(start + 1, end, mem)
            mem[start] = max(rob, skip)
            return mem[start]
        return max(dfs(0, len(nums)-1, {}), dfs(1, len(nums), {}))