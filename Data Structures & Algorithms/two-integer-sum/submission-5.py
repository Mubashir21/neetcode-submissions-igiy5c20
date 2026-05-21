class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in maps:
                maps[nums[i]] = i
            else:
                return [maps[diff], i]
        