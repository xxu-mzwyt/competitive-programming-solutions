# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def findMaxAncestorDiff(root):
            try:
                if root.left == None and root.right == None:
                    return {"max": root.val, "min": root.val, "rslt": -1}
                elif root.left == None:
                    rsltRight = findMaxAncestorDiff(root.right)
                    return {
                        "max": max(root.val, rsltRight["max"]),
                        "min": min(root.val, rsltRight["min"]),
                        "rslt": max(
                            rsltRight["rslt"],
                            abs(root.val - rsltRight["max"]),
                            abs(root.val - rsltRight["min"]),
                        ),
                    }
                elif root.right == None:
                    rsltLeft = findMaxAncestorDiff(root.left)
                    return {
                        "max": max(root.val, rsltLeft["max"]),
                        "min": min(root.val, rsltLeft["min"]),
                        "rslt": max(
                            rsltLeft["rslt"],
                            abs(root.val - rsltLeft["max"]),
                            abs(root.val - rsltLeft["min"]),
                        ),
                    }
                else:
                    rsltRight = findMaxAncestorDiff(root.right)
                    rsltLeft = findMaxAncestorDiff(root.left)
                    return {
                        "max": max(root.val, rsltRight["max"], rsltLeft["max"]),
                        "min": min(root.val, rsltRight["min"], rsltLeft["min"]),
                        "rslt": max(
                            rsltLeft["rslt"],
                            rsltRight["rslt"],
                            abs(root.val - rsltLeft["max"]),
                            abs(root.val - rsltLeft["min"]),
                            abs(root.val - rsltRight["max"]),
                            abs(root.val - rsltRight["min"])
                        ),
                    }
            except:
                print(root)

        return findMaxAncestorDiff(root)["rslt"]
