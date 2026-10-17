class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevStart, prevEnd = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
                if prevEnd > intervals[i][1]:
                    prevEnd = intervals[i][1]
            else:
                prevStart, prevEnd = intervals[i][0], intervals[i][1]
        return res
