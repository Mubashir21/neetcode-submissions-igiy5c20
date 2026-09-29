class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []
        heap = []

        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))
        
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)

        return res