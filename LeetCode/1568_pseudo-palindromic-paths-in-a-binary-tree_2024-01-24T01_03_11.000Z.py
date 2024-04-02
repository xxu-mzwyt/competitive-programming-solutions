# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def findPPPaths(root, freq):
            if not root:
                return 0

            rsltLeft = 0
            rsltRight = 0

            freq[root.val] += 1
            if freq[root.val] % 2 == 0:
                freq[0] -= 1
            else:
                freq[0] += 1

            if root.left:
                rsltLeft = findPPPaths(root.left, freq)
            if root.right:
                rsltRight = findPPPaths(root.right, freq)

            validPath = freq[0] <= 1
            freq[root.val] -= 1
            if freq[root.val] % 2 == 0:
                freq[0] -= 1
            else:
                freq[0] += 1

            if (not root.left) and (not root.right):
                if validPath:
                    return 1
                else:
                    return 0

            return rsltLeft + rsltRight

        freqArr = [0] * 10
        return findPPPaths(root, freqArr)      
        