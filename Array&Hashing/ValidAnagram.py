class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = dict()

        for c in s:
            sDict[c] = sDict.setdefault(c, 0) + 1

        tDict = dict()
        for c in t:
            tDict[c] = tDict.setdefault(c, 0) + 1
        
        return sDict == tDict