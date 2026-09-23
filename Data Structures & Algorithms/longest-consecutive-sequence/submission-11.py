class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni = set(nums)
        res = 0

        for index, num in enumerate(nums):
            if (num - 1) not in uni:
                i = num
                count = 0
                while i in uni:
                    count += 1
                    i += 1
                res = max(res, count)
        return res