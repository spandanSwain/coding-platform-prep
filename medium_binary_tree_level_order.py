# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        if not root: return []
        q = [root, None] # main queue
        ans, temp = [], []
        while q:
            curr_node = q.pop(0)
            if curr_node == None:
                ans.append(temp)
                temp = []
                if not q: return ans
                else: q.append(None)
            else:
                temp.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
        return ans
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/