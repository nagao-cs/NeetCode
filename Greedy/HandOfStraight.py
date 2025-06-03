from collections import Counter
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        # hand[0]~hand[0]+grupeSize-1まで連続した値があるはず
        # これらを取り除いた後のリストも繰り返す
        table = Counter(hand)
        hand.sort()
        numGroup = n // groupSize
        for card in hand:
            if table[card]:
                head = card
                table[card] -= 1
                for i in range(1, groupSize):
                    if table[card+i]:
                        table[card+i] -= 1
                    else:
                        return False

        return True
                
