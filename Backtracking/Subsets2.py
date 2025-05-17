class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = list([])
        nums.sort()
        def backtrack(start: int, subset) -> None:
            if subset[:] not in output:
                output.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()

        backtrack(0, [])
        return output