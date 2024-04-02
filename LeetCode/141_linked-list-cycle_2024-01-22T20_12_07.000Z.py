# https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        if curr == None:
            return False
        while curr.next:
            if curr.val == None:
                return True
            curr.val = None
            curr = curr.next
        return False


        