class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key=lambda x:x[0])
        # before = len(intervals)
        # merged = [intervals[0]]

        # for start, end in intervals[1:]:
        #     lastEnd = merged[-1][1]
        #     if start <= lastEnd:
        #         merged[-1][1] = max(lastEnd, end)
        #     else:
        #         merged.append([start, end])
        # after = len(merged)
        # return before - after

        intervals.sort(key=lambda x:x[0])
        lastEnd = intervals[0][1]
        count = 0

        for start, end in intervals[1:]:
            if start < lastEnd:
                count += 1
                lastEnd = min(end, lastEnd)
            else:
                lastEnd = end
        return count