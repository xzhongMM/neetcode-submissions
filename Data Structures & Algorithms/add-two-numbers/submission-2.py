# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val == 0:
            return l2
        elif l2.val == 0:
            return l1

        carryOver = False
        result = ListNode(0)
        resultHead = result

        #while neither number has reached the end
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            total = val1 + val2 + carryOver

            if total >= 10:
                carryOver = True
                total -= 10
            else:
                carryOver = False

            result.next = ListNode(total)
            result = result.next
            l1 = l1.next
            l2 = l2.next

        #if l1 & l2 are different in length
        #if l1 still has remaining digits
        while l1:
            cur = l1.val + carryOver
            if carryOver and cur >= 10:
                cur -= 10
            elif cur < 10:
                carryOver = False
            result.next = ListNode(cur)
            result = result.next
            l1 = l1.next
        #if l2 still has remaining digits
        while l2:
            cur = l2.val + carryOver
            if carryOver and cur >= 10:
                cur -= 10
            elif cur < 10:
                carryOver = False
            result.next = ListNode(cur)
            result = result.next
            l2 = l2.next

        #if there's a left over carry
        if carryOver:
            result.next = ListNode(1)

        return resultHead.next
