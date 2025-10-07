from typing import List
import bisect
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # 前の雨の日より遅く、次の雨の日よりも速いdryの日を探すために二分探索をする
        n = len(rains)
        ans = [-1 for _ in range(n)]

        last_rain = dict() # 各地に最後に雨が降った日を記録する
        dry_days = list() # 現在の乾燥に使える日を順に入れる

        for day, rain_city in enumerate(rains):
            if rain_city == 0:
                # 雨が降らない日(乾燥に使える日)を追加
                dry_days.append(day)
            else:
                if rain_city not in last_rain:
                    last_rain[rain_city] = day
                else:
                    if not dry_days:
                        # 乾燥に使える日がないなら[]を返す
                        return []
                    last_day = last_rain[rain_city]
                    # last_day以上day以下のdry_dayの内最小のものを見つける
                    # print(bisect.bisect(dry_days, last_day), dry_days)
                    dry_day_idx = bisect.bisect(dry_days, last_day)
                    if dry_day_idx == len(dry_days):
                        # last_dayよりも前の乾燥に使える日がない
                        return []
                    dry_day = dry_days[dry_day_idx]
                    if dry_day < last_day:
                        return []
                    else:
                        ans[dry_day] = rain_city
                        last_rain[rain_city] = day
                        del dry_days[dry_day_idx]
        
        for dry_day in dry_days:
            ans[dry_day] = 1
        return ans