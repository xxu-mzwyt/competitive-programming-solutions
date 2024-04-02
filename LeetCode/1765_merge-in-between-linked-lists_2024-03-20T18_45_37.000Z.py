# https://leetcode.com/problems/merge-in-between-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        first = ListNode(None, list1)
        head1 = first
        head1Ind = 0  # the index of head1.next
        while head1Ind < a:
            head1 = head1.next
            head1Ind += 1
        temp = head1.next
        head1.next = list2  # list1[a-1] = list2
        head1 = temp
        while head1Ind < b + 1:
            head1 = head1.next
            head1Ind += 1
        head2 = list2
        while head2.next != None:
            head2 = head2.next
        head2.next = head1  # list2[-1] = list1
        return first.next
        
        
        
        