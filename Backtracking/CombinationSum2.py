# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         output = list()
#         if sum(candidates) < target:
#             return output

#         def backtrack(nums, candidates):
#             if sum(nums) == target:
#                 nums.sort()
#                 if nums not in output:
#                     output.append(nums)
#                 return
#             if sum(nums) > target:
#                 return 
#             for i in range(len(candidates)):
#                 if sum(nums) + candidates[i] > target:
#                     break
#                 backtrack(nums+[candidates[i]], candidates[i+1:])
#         candidates.sort()
#         backtrack([], candidates)
#         return output

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. ソートしておくことで同じ数の重複処理と早期終了が可能に
        candidates.sort()
        results = []
        combination = []

        def backtrack(start: int, current_sum: int):
            if current_sum == target:
                # 深さ優先で構築済み combination のコピーを追加
                results.append(combination.copy())
                return
            # 早期終了: current_sum > target の場合
            if current_sum > target:
                return

            previous = -1  # 同じ値の組み合わせをスキップするためのガード
            for i in range(start, len(candidates)):
                num = candidates[i]
                # sum + num が target を超えるなら以降も大きいのでブレイク
                if current_sum + num > target:
                    break
                # 重複候補のスキップ
                if num == previous:
                    continue

                # 選択 & 再帰
                combination.append(num)
                backtrack(i + 1, current_sum + num)
                combination.pop()
                previous = num

        backtrack(0, 0)
        return results
