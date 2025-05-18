class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.setdefault(num, 0) + 1
        
        freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        
        output = [item[0] for item in freq[:k]]
        return output