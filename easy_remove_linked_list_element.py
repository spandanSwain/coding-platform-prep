# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val: head = head.next # start checking from first node
        temp = head
        while temp and temp.next:
            if temp.next.val == val and temp.next: temp.next = temp.next.next # if yes, then next points to next's next
            else: temp = temp.next # else normal traverse
        return head
# https://leetcode.com/problems/remove-linked-list-elements/submissions/1771539382/