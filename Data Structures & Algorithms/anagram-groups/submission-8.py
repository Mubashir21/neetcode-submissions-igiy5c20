from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        maps = defaultdict(list)
        res = []

        for i, word in enumerate(strs):
            word = ("").join(sorted(word))
            maps[word].append(i)

        for vals in maps.values():
            temp = []

            for i in vals:
                temp.append(strs[i])
            res.append(temp)
        return res