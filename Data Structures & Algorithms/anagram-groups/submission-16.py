class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)

        for word in strs:
            key = ("").join(sorted(word))
            maps[key].append(word)
        return [values for values in maps.values()]