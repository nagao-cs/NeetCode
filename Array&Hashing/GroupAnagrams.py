class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = list()
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [strs]
        hashtable = dict()
        for chars in strs:
            key = str(sorted(chars))
            hashtable.setdefault(key, []).append(chars)
        
        for anagram in hashtable:
            output.append(hashtable[anagram])
        return output
