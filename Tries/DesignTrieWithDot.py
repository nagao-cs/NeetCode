class WordDictionary:
    class ListNode:
        def __init__(self):
            self.children = dict()
            self.is_end = False

    def __init__(self):
        self.head = self.ListNode()

    def addWord(self, word: str) -> None:
        node = self.head
        for c in word:
            if c not in node.children:
                node.children[c] = self.ListNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.head
        for i in range(len(word)):
            if word[i] == '.':
                #dotがでたら、現在の文字の子供すべてをdfsする
                for key, node in node.children.items():
                    if self.search_from_middle(node, word[i+1:]):
                        return True
                return False
            elif word[i] not in node.children:
                return False
            node = node.children[word[i]]
        return node.is_end
    
    def search_from_middle(self, node, word: str) -> bool:
        for i in range(len(word)):
            if word[i] == '.':
                #dotがでたら、現在の文字の子供すべてをdfsする
                for key, node in node.children.items():
                    if self.search_from_middle(node, word[i+1:]):
                        return True
                return False
            elif word[i] not in node.children:
                return False
            node = node.children[word[i]]
        return node.is_end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)