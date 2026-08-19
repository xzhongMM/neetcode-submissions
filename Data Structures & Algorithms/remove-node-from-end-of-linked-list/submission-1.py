# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmpHead = head
        #find length of list
        length = 0
        while tmpHead:
            length += 1
            tmpHead = tmpHead.next
        
        nToRemove = length - n
        if nToRemove <= 0:
            return head.next

        #locate one node before node to remove
        nodeToRemove = head
        for i in range(nToRemove-1):
            nodeToRemove = nodeToRemove.next

        if nodeToRemove is None:
            newHead = head.next
            head = null
            return newHead
        else:
            nodeToRemove.next = nodeToRemove.next.next
            return head

