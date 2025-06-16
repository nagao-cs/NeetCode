from typing import List
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidate = set(i for i in range(len(triplets)))
        for k in range(3):
            x = target[k]
            # k番目の要素がtarget[k]以下のtripletsのみが探索範囲になる
            new_candidate = set()
            for i in candidate:
                if triplets[i][k] <= x:
                    new_candidate.add(i)
            candidate = new_candidate
        # print(candidate)
        for k in range(3):
            found = False
            for i in candidate:
                if triplets[i][k] == target[k]:
                    found = True
                    break
            if not found:
                return False
        return True