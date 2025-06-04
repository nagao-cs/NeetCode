from typing import Optional
class Node:
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None        
        #オリジナルのリストノードのnext,randomの値に対応するノードが辞書にあるか確認する
        #対応するノードがあればコピーノードのnext,randomはそのノードにする
        #なければ新たなノードを作り、辞書に追加する
        #オリジナル、コピーを次のノードに移動する
        nodeTable = dict()
        origin = head
        copy_head = Node(origin.val)
        nodeTable[head] = copy_head
        copy = copy_head

        while origin:
            assert origin is not None # 型チェッカー対策
            assert copy is not None    
            if origin.next:
                if origin.next in nodeTable:
                    copy.next = nodeTable[origin.next]
                else:
                    nodeTable[origin.next] = Node(origin.next.val)
                    copy.next = nodeTable[origin.next]
            else:
                copy.next = None
            if origin.random:
                if origin.random in nodeTable:
                    copy.random = nodeTable[origin.random]
                else:
                    nodeTable[origin.random] = Node(origin.random.val)
                    copy.random = nodeTable[origin.random]
            else:
                copy.random = None
            origin = origin.next
            copy = copy.next

        return copy_head                