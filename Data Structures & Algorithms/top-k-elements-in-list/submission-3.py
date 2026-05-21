class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = defaultdict(int)

        for num in nums:
            maps[num] = 1 + maps[num]
        
        tups = []
        for key, value in maps.items():
            tups.append((value, key))
        tups.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(tups[i][1])
        return res