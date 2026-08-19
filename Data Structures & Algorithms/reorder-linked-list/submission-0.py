# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        l2 = head.next

        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next

        #reverse the second list
        current = l1.next
        prev = l1.next = None
        while current:
            curnext = current.next
            current.next = prev
            prev = current
            current = curnext

        #prev is second list's new head
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first =  tmp1
            second = tmp2

            
        