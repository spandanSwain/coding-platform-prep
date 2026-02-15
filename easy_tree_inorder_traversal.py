# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        # INORDER = LEFT ROOT RIGHT
        # PREORDER = ROOT LEFT RIGHT
        ans = []
        self.build(root, ans)
        return ans
    def build(self, root, ans):
        if root:
            self.build(root.left, ans)
            ans.append(root.val)
            self.build(root.right, ans)
# https://leetcode.com/problems/binary-tree-inorder-traversal/