class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index = {}

        for i, num in enumerate(nums):
            index[num] = i

        for i, num in enumerate(nums):
            diff = target - num

            if diff in index and index[diff] != i:
                return [i, index[diff]]