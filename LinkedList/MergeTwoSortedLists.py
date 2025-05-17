# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # 両方のリストが空の場合、空のリストを返す
        if not list1 and not list2:
            return None
        # 一方のリストが空の場合、もう一方のリストを返す
        elif not list1:
            return list2
        elif not list2:
            return list1

        # リストのヘッドを決定
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        # 現在のノードをヘッドに設定
        current_node = head

        # どちらかのリストが空になるまでループ
        while list1 and list2:
            if list1.val < list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            current_node = current_node.next

        # どちらかのリストがまだ要素を持っている場合、それを追加
        current_node.next = list1 if list1 else list2

        return head


