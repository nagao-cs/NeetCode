from typing import List
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        m = len(mana) # ポーションの数
        n = len(skill) # 魔法使いの人数
        
        finish_time = [0 for _ in range(n)]
        now = 0

        for wiz in range(n):
            finish_time[wiz] = now + (skill[wiz]*mana[0])
            now = finish_time[wiz]
        
        for potion in range(1, m):
            now = finish_time[0] + skill[0] * mana[potion] # 1人目のwizardがpotionを終わった時間
            for wiz in range(1, n):
                time = skill[wiz] * mana[potion] # wizがpotionを完了するのにかかる時間
                now = max(now, finish_time[wiz]) + time
            finish_time[n-1] = now
            for wiz in range(n-2, -1, -1):
                time = skill[wiz+1] * mana[potion] # wiz+1がpotionを完了するのにかかる時間
                finish_time[wiz] = finish_time[wiz+1] - time
        
        # print(finish_time)
        return finish_time[n-1]
                