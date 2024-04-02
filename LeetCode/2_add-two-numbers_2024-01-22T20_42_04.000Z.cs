// https://leetcode.com/problems/add-two-numbers

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode rslt = new ListNode{};
        ListNode curr = rslt;
        ListNode last = rslt;

        int carry = 0;
        while (l1 != null && l2 != null) {
            curr.val = l1.val + l2.val + carry;
            carry = 0;
            if (curr.val >= 10) {
                curr.val -= 10;
                carry = 1;
            }
            curr.next = new ListNode{};
            last = curr;
            curr = curr.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        curr.val = carry;
        while (l1 != null) {
            curr.val = l1.val + carry;
            carry = 0;
            if (curr.val >= 10) {
                curr.val -= 10;
                carry = 1;
            }
            curr.next = new ListNode{};
            last = curr;
            curr = curr.next;
            l1 = l1.next;
        }
        while (l2 != null) {
            curr.val = l2.val + carry;
            carry = 0;
            if (curr.val >= 10) {
                curr.val -= 10;
                carry = 1;
            }
            curr.next = new ListNode{};
            last = curr;
            curr = curr.next;
            l2 = l2.next;
        }
        curr.val = carry;
        if (curr.val == 0) {
            last.next = null;
        }
        return rslt;    
    }
}