class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        same = defaultdict(list)

        for i, word in enumerate(strs):
            new = ("").join(sorted(word))
            same[new].append(strs[i])
        
        return [value for value in same.values()]