from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        update = sorted(list(count.items()), key=lambda item: item[1],reverse=True)
        return [update[i][0] for i in range(k)]