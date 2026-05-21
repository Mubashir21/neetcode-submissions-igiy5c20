class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        res = 0
        for num in nums:
            if (num - 1) not in numSet:
                count = 0
                cur = num
                while cur in numSet:
                    cur += 1
                    count += 1
                res = max(count, res)
        return res