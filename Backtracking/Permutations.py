class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = list()

        def backtrack(permutation, nums:list):
            if len(nums) == 0:
                output.append(permutation)
                return

            for i in range(len(nums)):
                backtrack(permutation+[nums[i]], nums[:i]+nums[i+1:])


        backtrack([], nums)
        return output