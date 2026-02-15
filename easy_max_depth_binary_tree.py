# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if not root: return 0
        depth, q = 0, [root, None]
        while q:
            curr = q.pop(0)
            if curr == None:
                depth+=1
                if not q: return depth
                else: q.append(None)
            else:
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# this one doesn't properly align but yeah makeshift
def depth_using_DFS(root):
    if not root: return 0
    left = 1 + depth_using_DFS(root.left)
    right = 1 + depth_using_DFS(root.right)
    return max(left, right)
# print(f"Depth using recursion and DFS: {depth_using_DFS(root_node)}") # better use this