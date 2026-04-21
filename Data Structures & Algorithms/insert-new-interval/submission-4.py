class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = merged[-1][1]
            if start <= lastEnd:
                merged[-1][1] = max(lastEnd, end)
            else:
                merged.append([start, end])
        return merged
