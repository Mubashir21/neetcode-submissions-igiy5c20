class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for word in strs:
            seen[("").join(sorted(word))].append(word)
        res = []

        for key in seen.keys():
            temp = []
            for word in seen[key]:
                temp.append(word)
            res.append(temp)
        return res
