class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # this solution is an adaptation of the merge interval question
        # not the most optimal because list already sorted
        
        # if not intervals:
        #     return [newInterval]
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x:x[0])
        # merged = [intervals[0]]

        # for start, end in intervals[1:]:
        #     lastEnd = merged[-1][1]
        #     if start <= lastEnd:
        #         merged[-1][1] = max(lastEnd, end)
        #     else:
        #         merged.append([start, end])
        # return merged

        res = []

        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        res.append(newInterval)
        return res