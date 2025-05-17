class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int]):
            result.append(path[:])  # 現在の部分集合を追加

            for i in range(start, len(nums)):
                path.append(nums[i])        # 要素を追加
                backtrack(i + 1, path)      # 次の要素へ
                path.pop()                  # 元に戻す（バックトラック）

        backtrack(0, [])
        return result
