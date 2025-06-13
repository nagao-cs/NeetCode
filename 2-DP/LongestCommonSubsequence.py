class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # dp[i][j] は text1 の最初の i 文字と text2 の最初の j 文字における最長共通部分列の長さ
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                # text1[i-1] と text2[j-1] は現在の文字
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]