class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q: # if p is none and q is also none, then good
            return True
        if not p or not q: # if either of them is none, they are not same
            return False
        if p.val != q.val: # if value is not same, then they are clearly not same
            return False
        # check for every left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 

# https://leetcode.com/problems/same-tree/description/
# I tried by using inorder traversal list, and return it's comparison, but here we have to check if the structures are also same or not.