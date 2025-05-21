class LRUCache:
    class ListNode:
        def __init__(self, key=0, val=0, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.numNode = 0
        self.head = self.ListNode()
        self.tail = self.ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()

    def get(self, key: int) -> int:
        res = -1
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.add_to_head(node)
            res = node.val
        return res

    def put(self, key: int, value: int) -> None:
        #既存のノードの更新の場合
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.add_to_head(node)
            return
        #cacheにkeyがない場合
        if self.numNode >= self.capacity:
            #cacheにこれ以上はいらないなら、最後のノードを削除して先頭に新しいノードを追加する
            self.removeLast()
        new_node = self.ListNode(key=key, val=value)
        self.add_to_head(new_node)
        self.numNode += 1
        self.cache[key] = new_node
    
    def removeNode(self, node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next, node.prev = None, None
    
    def add_to_head(self, node) -> None:
        #nodeをListNodeの先頭に設置する
        if node == self.head.next:
            return 
        next_node = self.head.next #現在の先頭のノードをnext_node
        self.head.next = node
        node.prev = self.head
        node.next, next_node.prev = next_node, node
        # self.printcache()

    def removeLast(self) -> None:
        #ListNodeの最後のノードを削除する
        last = self.tail.prev
        last.prev.next = self.tail
        self.tail.prev = last.prev
        last.next, last.prev = None, None
        self.numNode -= 1
        self.cache.pop(last.key)

    def printcache(self):
        cache = "head->"
        node = self.head.next
        while node != self.tail:
            cache += f"{node.val}->"
            node = node.next
        cache += "tail"
        print(cache)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)