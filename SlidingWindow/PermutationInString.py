class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freaquence = dict()
        for s in s1:
            freaquence[s] = freaquence.setdefault(s, 0) + 1
        freaquence = sorted(freaquence.items(), key=lambda x: x[0])
        print(freaquence)

        i = 0
        hashtabel = dict()
        # i文字目
        while i < len(s2):
            if s2[i] in freaquence and i + len(s1) <= len(s2):
                for s in s2[i : i + len(s1)]:
                    hashtable[s] = hashtable.setdefault(s, 0) + 1
                hashtable = sorted(hashtable.items(), key=lambda x: x[0])
                print(s2[i : i + len(s1)])
                print(hashtable)
                if freaquence == hashtable:
                    return True
                else:
                    hashtable = dict()
            i += 1
        return False