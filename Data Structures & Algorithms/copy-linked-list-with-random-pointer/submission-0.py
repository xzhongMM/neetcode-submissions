"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        newHead = Node(0)
        newList = newHead
        reference = {}
        oldList = head
        
        #iterating through old list to copy value and next first
        while oldList:
            cur = Node(oldList.val)
            reference[oldList] = cur
            if newList:
                newList.next = cur
                newList = newList.next
                oldList = oldList.next

        #reset oldList and iterate through old list again to copy new random nodes
        oldList = head

        while oldList:
            if oldList.random:
                reference[oldList].random = reference[oldList.random]
            else:
                reference[oldList].random = None
            oldList = oldList.next

        return newHead.next