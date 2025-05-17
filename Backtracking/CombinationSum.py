class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = list()
        
        def backtrack(nums:list, candidates:list):
            if sum(nums) == target:
                output.append(nums)
                return
            if sum(nums) < target:
                for i in range(len(candidates)):
                    backtrack(nums+[candidates[i]], candidates[i:])
                
        backtrack([], candidates)
        
        return output