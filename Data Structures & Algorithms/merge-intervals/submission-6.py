class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        n = len(intervals)
        curStart, curEnd = intervals[0][0], intervals[0][1]

        for i in range(1, n):
            if curEnd >= intervals[i][0]:
                curStart = min(curStart, intervals[i][0])
                curEnd = max(curEnd, intervals[i][1])
            else:
                res.append([curStart, curEnd])
                curStart = intervals[i][0]
                curEnd = intervals[i][1]
        res.append([curStart, curEnd])
        return res