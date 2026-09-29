class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            water = width * height
            res = max(res, water)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res