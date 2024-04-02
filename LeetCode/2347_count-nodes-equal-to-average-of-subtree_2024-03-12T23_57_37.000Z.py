# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def findAverage(root):
            leftSize = rightSize = 0
            leftSum = rightSum = 0
            leftRslt = rightRslt = 0
            if root.left != None:
                leftSize, leftSum, leftRslt = findAverage(root.left)
            if root.right != None:
                rightSize, rightSum, rightRslt = findAverage(root.right)
            currSize = leftSize + rightSize + 1
            currSum = leftSum + rightSum + root.val
            currRslt = leftRslt + rightRslt + (currSum // currSize == root.val)
            # print(root.val, currSum / currSize, currSize, currSum, currRslt)
            return currSize, currSum, currRslt
        return findAverage(root)[2]
        