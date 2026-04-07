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

        # counter = {}
        # for num in nums:
        #     counter[num] = counter.get(num, 0) + 1

        # heap = []
        # for num, freq in counter.items():
        #     heapq.heappush(heap, (freq, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # return [num for freq, num in heap]

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) >= k:
                    return res

