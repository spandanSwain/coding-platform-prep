# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        if not root: return root
        output = []

        if not root.left and not root.right:
            output.extend(f"{root.val}")
        if root.left:
            output.extend(self.recur(root.left, f"{root.val}"))
        if root.right:
            output.extend(self.recur(root.right, f"{root.val}"))
        return output

    def recur(self, root, s: str) -> str:
        curr = f"{s}->{root.val}"
        if not root.left and not root.right:
            return [curr]
        r = []
        if root.left:
            r.extend(self.recur(root.left, curr))
        if root.right:
            r.extend(self.recur(root.right, curr))
        return r
# https://leetcode.com/problems/binary-tree-paths/description/
"""
It is a DFS Traversal
"""