# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode()
        d_i = dummy
        temp = head
        collect_unique = []

        while temp:
            if temp.val not in collect_unique:
                collect_unique.append(temp.val)
                d_i.next = ListNode(temp.val)
                d_i = d_i.next
            temp = temp.next
        return dummy.next
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# solved it by own...yesss😭😭