# https://leetcode.com/problems/remove-nodes-from-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def remove(head):
            if head == None:
                return -1, False
            else:
                maxVal, toRemove = remove(head.next)
                if toRemove:
                    head.next = head.next.next
                return max(maxVal, head.val), head.val < maxVal
        if remove(head)[1]:
            head = head.next
        return head
                    


        