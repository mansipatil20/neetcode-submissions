# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_list = ListNode()
        tail = new_list
        p1_head = list1
        p2_head = list2
        while p1_head and p2_head:
            if p1_head.val < p2_head.val:
                tail.next = p1_head
                p1_head = p1_head.next
            else:
                tail.next = p2_head
                p2_head = p2_head.next
            tail = tail.next
        if p1_head:
            tail.next = p1_head
        if p2_head:
            tail.next = p2_head
        return new_list.next

        