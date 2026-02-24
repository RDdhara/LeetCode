# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, n):
        if not root:
            return 0
        n = n * 2 + root.val

        if not root.left  and not root.right:
            return n

        return self.solve(root.left, n) + self.solve(root.right, n)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.solve(root, 0)
