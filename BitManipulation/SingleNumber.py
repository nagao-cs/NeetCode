class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = set()
        for num in nums:
            if num not in single:
                single.add(num)
            else:
                single.discard(num)
        
        return single.pop()