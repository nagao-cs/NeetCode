from pprint import pprint
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[True if i==j==0 else False for j in range(n+1)] for i in range(m+1)]
        # dp[i][j]はsのi文字目までと,pのj文字目までがマッチしているか
        # 空文字と空文字はマッチするからdp[0][0]はTrue
        prev = ''
        for i in range(m+1):
            for j in range(1, n+1):
                char = p[j-1]
                if i == 0:
                    if char == '*' and dp[i][j-2]:
                        dp[i][j] = True
                else:
                    if char == '.':
                        # sとpの１文字前までがマッチしていれば,sのi文字目までとpのj文字目までがマッチする
                        if dp[i-1][j-1]:
                            dp[i][j] = True
                    elif char == '*':
                        if prev == '.' and (dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]):
                            # １つ前が'.'なら任意の文字とマッチし、かつ空文字でもいいから必ずマッチする
                            dp[i][j] = True
                        else:
                            if dp[i-1][j-1] and prev == s[i-1]:
                                # 1回以上繰り返す場合
                                dp[i][j] = True
                            elif prev == s[i-1] and dp[i-1][j]:
                                dp[i][j] = True
                            elif dp[i][j-2]:
                                # 繰り返し0回でマッチする場合
                                dp[i][j] = True
                    else:
                         # sとpの１文字前までがマッチしているかつ、現在見ている文字が一致している
                        if dp[i-1][j-1] and s[i-1] == char:
                            dp[i][j] = True
                    prev = char
                # print(f"{i}文字目 s={s[:i]}, p={p}")
                # pprint(dp[:i+1])
                # print()
        print(f"s:{s}, p:{p}")
        pprint(dp)
        return dp[-1][-1]