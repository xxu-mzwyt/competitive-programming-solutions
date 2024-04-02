# https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        ind = 0
        while curr != None:
            if type(curr.val) != int:
                return curr.val[1]
            curr.val = (curr.val, curr)
            curr = curr.next
        return None
        