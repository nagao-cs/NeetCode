from itertools import zip_longest
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = map(int, version1.split('.'))
        v2_parts = map(int, version2.split('.'))

        for v1, v2 in zip_longest(v1_parts, v2_parts, fillvalue=0):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0