class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 0:
            return None

        dp = [[i==j for i in range(len(s))] for j in range(len(s))]
        #dp[i][j]はsのiからj文字目がpalindrome
        #dp[i][j]がtrueになるには、dp[i-1][j-1]がtrueかつs[i]==s[j]
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True

        i = 0
        for padding in range(2,len(s)):
            j = i + padding
            while j < len(s):
                #s[i][j]について
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                i += 1
                j += 1
            i = 0 

        # for k in range(len(dp)):
        #     print(dp[k])

        MAX = -1
        start = 0
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if dp[i][j] and j-i > MAX:
                    MAX = j-i
                    start = i
                    # print(start, MAX)
        return s[start:start+MAX+1]
