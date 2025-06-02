from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
        counter_t = Counter(t)
        res = ''
        min_window = m+1
        l, r = 0, 0
        counter_s = Counter()
        while l < m-n+1:
            # print(f"(l,r):({l},{r})")
            #tの文字をすべて含むまでrを進める
            if (counter_s & counter_t) != counter_t and r < m:
                char = s[r]
                counter_s[char] += 1
                r += 1
            #tの文字をすべて含んでいる間はlを進める
            else: #(counter_s & counter_t) == counter_t:
                if r-l < min_window and (counter_s & counter_t) == counter_t:
                    res = s[l:r] #仮の答え
                    min_window = r-l
                char = s[l]
                counter_s[char] -= 1
                l += 1
            # else:
            #     l += 1

        return res
