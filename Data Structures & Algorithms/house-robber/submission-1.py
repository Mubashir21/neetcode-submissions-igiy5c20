class Solution:
    def rob(self, nums: List[int]) -> int:
        # left, right = 0, 0

        # for i in range(len(nums)):
        #     temp = right
        #     right = max(left + nums[i], right)
        #     left = temp
        # return right
        
        maps = {}
        def dfs(house):
            if house == len(nums) - 1:
                return nums[house]
            if house >= len(nums):
                return 0
            if house in maps:
                return maps[house]
            
            maps[house] = max(dfs(house + 2) + nums[house], dfs(house + 1))
            return maps[house]
        return dfs(0)