class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda x: x[0])
        # merged = [intervals[0]]

        # for start, end in intervals[1:]:
        #     lastEnd = merged[-1][1]
        #     if start <= lastEnd:
        #         merged[-1][1] = max(lastEnd, end)
        #     else:
        #         merged.append([start, end])
        # return merged

        intervals.sort(key=lambda x:x[0])
        merge = [[intervals[0][0], intervals[0][1]]]

        for start, end in intervals:
            lastEnd = merge[-1][1]
            if start <= lastEnd:
                merge[-1][1] = max(end, lastEnd)
            else:
                merge.append([start, end])
        return merge
        