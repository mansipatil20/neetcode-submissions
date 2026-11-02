# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode(0)
        carry = 0
        temp_head = list3
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val3 = val1 + val2 + carry
            if val3 > 9:
                carry = 1
            else: 
                carry = 0
            list3.next = ListNode(val3 % 10)
            list3 = list3.next


            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return temp_head.next



            

        