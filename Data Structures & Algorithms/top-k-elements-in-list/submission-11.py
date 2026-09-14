class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for num, freq in freq.items():
            heapq.heappush(heap, (-freq, num))
        return [(heapq.heappop(heap))[1] for _ in range(k)]