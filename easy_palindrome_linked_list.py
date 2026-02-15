# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        i = self.ReverseList(slow)
        j = head
        while i and j:
            if i.val != j.val: return False
            i, j = i.next, j.next
        return True

    def ReverseList(self, head):
        prev, temp, nxt = None, head, None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        return prev
# https://leetcode.com/problems/palindrome-linked-list/