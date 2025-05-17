class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #wordの1文字目を探す
        #wordの1文字目のますを探索済みにする
        #周囲4マスに2文字目以降があるか探す
        #wordが空文字になったらtrue
        if word == '':
            return True
        
        m = len(board)
        n = len(board[0])
        # serched = [[False for _ in range(n)] for __ in range(m)]
        searched = set()

        def backtrack(pos, word):
            # print(pos, word, searched)
            if word == '':
                return True
            #pos = [i, j]
            i, j = pos[0], pos[1]
            next = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
            for i, j in next:
                if ((i, j) in searched) or i < 0 or m <= i or j < 0 or n <= j:
                    continue
                if board[i][j] == word[0]:
                    searched.add((i, j))
                    if backtrack([i, j], word[1:]):
                        return True
                    else:
                        searched.discard((i, j))
                
                

            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    searched.add((i, j))
                    if backtrack([i, j], word[1:]):
                        return True
                    else:
                        searched.clear()
        
        return False
