# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for h in lists:
            current = h
            while current:
                heapq.heappush(heap, current.val)
                current = current.next
        dummy_node = ListNode()
        head = dummy_node
        while heap:
            pop_val = heapq.heappop(heap)
            new_node = ListNode(pop_val)
            head.next = new_node
            head = head.next
        dummy_node = dummy_node.next
        return dummy_node