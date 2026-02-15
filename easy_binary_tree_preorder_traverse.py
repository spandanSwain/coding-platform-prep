# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        self.build(root, res)
        return res
    def build(self, root, res):
        if root:
            res.append(root.val)
            self.build(root.left, res)
            self.build(root.right, res)
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/