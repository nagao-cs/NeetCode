class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie_tree = Trie()
        for word in wordDict:
            trie_tree.insert(word)

        dp = [False] * len(s)
        #dp[i]はs[i]がwordDictで構成できるか
        for i in range(len(s)):
            if trie_tree.find(s[:i+1]):
                dp[i] = True
                continue
            j = i-1
            while j >= 0:
                if dp[j] and trie_tree.find(s[j+1:i+1]):
                    dp[i] = True
                    break
                j -= 1            
        return dp[len(s)-1]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def find(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end