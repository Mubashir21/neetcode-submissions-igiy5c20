class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        magic = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in magic:
                count = 1
                cur = num
                while cur + 1 in magic:
                    cur += 1
                    count += 1
                res = max(res, count)
        return res