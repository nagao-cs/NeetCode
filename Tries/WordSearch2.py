from typing import List
from typing import Optional
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        res = set()
        def dfs(i, j, visited, trieNode):
            char = self.board[i][j]
            if char not in trieNode.children:
                return
            trieNode = trieNode.children[char]
            if trieNode.val:
                res.add(trieNode.val)
                trieNode.val = None
            visited[i][j] = True
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                next_i, next_j = i+dr, j+dc
                if (0 <= next_i < self.m and 0 <= next_j < self.n) and (not visited[next_i][next_j]):
                    dfs(next_i, next_j, visited, trieNode)
            visited[i][j] = False
        
        for i in range(self.m):
            for j in range(self.n):
                visited = [[False for _ in range(self.n)] for __ in range(self.m)]
                dfs(i, j, visited, self.trie.root)

        return list(res)        

class Trie:
    class Node:
        def __init__(self):
            self.children = dict()
            self.val: Optional[str] = None

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = self.Node()
            node = node.children[c]
        node.val = word

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return node.val == word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True