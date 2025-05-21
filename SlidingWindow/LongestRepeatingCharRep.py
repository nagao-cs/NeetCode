class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = dict() #各文字の出現回数
        max_freq = 0 #現在のwindowで最頻の文字の出現回数
        max_len = 0 #最長の連続した文字列

        for r in range(len(s)):
            char = s[r]
            count[char] = count.get(char, 0) + 1

            max_freq = max(max_freq, count[char])
            window_size = r - l + 1
            if max_freq + k < window_size:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)

        return max_len