# https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findDiameter(root):
            leftDiameter = leftDepth = -1
            rightDiameter = rightDepth = -1
            if root.left:
                leftDiameter, leftDepth = findDiameter(root.left)
            if root.right:
                rightDiameter, rightDepth = findDiameter(root.right)
            return max(leftDiameter, rightDiameter, leftDepth + rightDepth + 2), max(leftDepth, rightDepth) + 1
        return findDiameter(root)[0]
        