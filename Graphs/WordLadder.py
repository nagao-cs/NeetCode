from collections import deque
import string
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        wordset = set(wordList)
        res = float('inf')
        que = deque()
        que.appendleft((beginWord, 1))
        while que:
            current, sequence = que.pop()
            # print(current, sequence)
            for i in range(n):
                for char in list(string.ascii_lowercase):
                    new_word = current[:i] + char + current[i+1:]
                    if new_word == endWord:
                        res = min(res, sequence+1)
                    elif new_word in wordset:
                        que.appendleft((new_word, sequence+1))
                        wordset.discard(new_word)
        
        if res == float('inf'):
            return 0
        return int(res)
