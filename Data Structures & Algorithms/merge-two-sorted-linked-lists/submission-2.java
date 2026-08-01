/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null){
            return list2;
        }
        else if(list2 == null){
            return list1;
        }

        ListNode cur1 = list1;
        ListNode cur2 = list2;
        ListNode prev = null;
        ListNode newHead = (cur1.val <= cur2.val) ? cur1 : cur2;

        while(cur1 != null && cur2 != null){
            if(cur1.val <= cur2.val){
                if(prev != null){
                    prev.next = cur1;
                }
                prev = cur1;
                cur1 = cur1.next;
            }
            else{
                if(prev != null){
                    prev.next = cur2;
                }
                prev = cur2;
                cur2 = cur2.next;
            }
        }
        if(cur1 == null){
            prev.next = cur2;
        }
        else if(cur2 == null){
            prev.next = cur1;
        }
        return newHead;
    }
}