class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size1 = len(s1)
        if size1 > len(s2):
            return False
        
        need = Counter(s1)
        window = Counter(s2[:size1])

        if window == need:
            return True
        
        for r in range(size1, len(s2)):
            window[s2[r]] += 1
            window[s2[r-size1]] -= 1

            if window[s2[r-size1]] == 0:
                del window[s2[r-size1]]
            
            if window == need:
                return True
        return False
