# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        self.build(root, res)
        return res
    def build(self, root, res):
        if root:
            self.build(root.left, res)
            self.build(root.right, res)
            res.append(root.val)
# https://leetcode.com/problems/binary-tree-postorder-traversal/