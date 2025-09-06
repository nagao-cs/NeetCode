from math import log, floor
from typing import List
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        count = 0

        def minOperation(query: List[int]) -> int:
            total = query[1] - query[0] + 1
            count = 0
            hashTable = {0: 0}
            base = query[0]
            while base < query[1]+1:
                key = floor(log(base, 4)) + 1
                top = min(4**key-1, query[1])
                hashTable[key] = top - base + 1
                base = top + 1

            for key in range(max(hashTable)):
                hashTable.setdefault(key, 0)

            while hashTable[0] != total:
                max_key = max(hashTable)
                if max_key == 1: 
                    count += (hashTable[1] // 2) + (hashTable[1] % 2)
                    hashTable[0] += hashTable[1]
                    hashTable[1] = 0
                else:
                    if hashTable[max_key] % 2 == 0:
                        count += hashTable[max_key] / 2
                        hashTable[max_key-1] += hashTable[max_key]
                    else:
                        count += (hashTable[max_key] // 2) + 1
                        hashTable[max_key-1] += hashTable[max_key]-1
                        hashTable[max_key-2] += 1
                    del hashTable[max_key]
                # print(f"hashTable: {hashTable}, count:{count}")

            return int(count)
        
        for query in queries:
            count += minOperation(query)
        
        return count