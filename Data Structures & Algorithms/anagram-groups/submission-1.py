from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sortedList = []

        # for word in strs:
        #     sortedList.append("".join(sorted(word)))
        
        # sortedMap = {}
        # for i, word in enumerate(sortedList):
        #     if word not in sortedMap:
        #         sortedMap[word] = [i]
        #     else:
        #         sortedMap[word].append(i)

        # final = []
        # for word in sortedMap:
        #     subFinal = []
        #     for index in sortedMap[word]:
        #         subFinal.append(strs[index])
        #     final.append(subFinal)
        # return final

        res = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())