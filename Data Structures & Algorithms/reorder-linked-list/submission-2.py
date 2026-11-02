# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        
        temp = slow.next
        slow.next = None
        prev = None
        # reverse the 2nd half
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        # merge the list
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2