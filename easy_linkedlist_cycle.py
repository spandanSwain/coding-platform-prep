# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        return False
# https://leetcode.com/problems/linked-list-cycle/description/
# The pos is not even a parameter, it is there to explain us
# This strategy is known as fast and slow pointer, fast goes 2 steps, slow goes one at a time
# Main aim is to check if there is a loop in the single linked list