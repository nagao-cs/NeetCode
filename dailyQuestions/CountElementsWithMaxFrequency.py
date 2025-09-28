from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = dict()
        max_freq = 0
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
            max_freq = max(max_freq, freq[num])
        
        count = max_freq * len(list(filter(lambda val: val == max_freq, freq.values())))

        
        return count