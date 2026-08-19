class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            seen[target - num] = i
        
        for i, num in enumerate(nums):
            if num in seen and i != seen[num]:
                return [i, seen[num]]