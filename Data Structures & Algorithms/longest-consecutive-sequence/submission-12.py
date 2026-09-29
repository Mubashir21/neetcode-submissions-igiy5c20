class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in uni:
                count = 0
                while num in uni:
                    num += 1
                    count += 1
                res = max(res, count)
        return res