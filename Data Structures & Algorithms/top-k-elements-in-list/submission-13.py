class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        res = []

        for num, reps in freq.items():
            heapq.heappush(heap, (-reps, num))
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res