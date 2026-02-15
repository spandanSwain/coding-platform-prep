# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
# https://leetcode.com/problems/invert-binary-tree/description/
"""
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""