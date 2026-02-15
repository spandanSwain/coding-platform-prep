# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, temp, nxt = None, head, None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt # we lost temp.next so use nxt as it knows what was next
        return prev # everything starts from prev
# https://leetcode.com/problems/reverse-linked-list