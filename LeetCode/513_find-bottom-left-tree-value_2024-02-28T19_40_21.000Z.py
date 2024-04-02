# https://leetcode.com/problems/find-bottom-left-tree-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def findDepthAndBL(root):
            leftDepth = rightDepth = -1
            leftVal = rightVal = None
            if root.left:
                leftDepth, leftVal = findDepthAndBL(root.left)
            if root.right:
                rightDepth, rightVal = findDepthAndBL(root.right)
            maxDepth = max(leftDepth, rightDepth) + 1
            if leftVal == None and rightVal == None:
                maxVal = root.val
            elif leftVal == None:
                maxVal = rightVal
            elif rightVal == None or leftDepth >= rightDepth:
                maxVal = leftVal
            else:
                maxVal = rightVal
            return maxDepth, maxVal 
        return findDepthAndBL(root)[1]
        