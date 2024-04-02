# https://leetcode.com/problems/remove-nodes-from-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # def ListNode2List(head: Optional[ListNode]) -> list:
        #     lst = []
        #     while head != None:
        #         lst.append(head.val)
        #         head = head.next
        #     return lst
        # def List2ListNode(lst: list) -> Optional[ListNode]:
        #     head = ListNode(lst[0])
        #     curr = head
        #     for val in lst[1:]:
        #         curr.next = ListNode(val)
        #         curr = curr.next
        #     return head
        # lst = ListNode2List(head)
        # lst.reverse()
        # outLst = []
        # currMax = -1
        # for val in lst:
        #     if val >= currMax:
        #         currMax = val
        #         outLst.append(val)
        # outLst.reverse()
        # return List2ListNode(outLst)
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
                    


        