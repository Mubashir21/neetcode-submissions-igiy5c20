import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashMap = {}

        # for num in nums:
        #     hashMap[num] = 1 + hashMap.get(num, 0)

        # arr = []
        # for num, cnt in hashMap.items():
        #     arr.append([cnt, num])
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res

        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]
