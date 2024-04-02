# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode(None, head)
        curr = first
        while curr != None:
            currRangeL = currRangeR = curr.next
            currSum = 0
            cut = False
            while currRangeR != None:
                currSum += currRangeR.val
                currRangeR = currRangeR.next
                if currSum == 0:
                    curr.next = currRangeR
                    cut = True
                    break
            if not cut:
                curr = curr.next
        return first.next
