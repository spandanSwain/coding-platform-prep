# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        temp = head

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1 # put l1 in new list
                list1 = list1.next # make l1 go forward
            else:
                temp.next = list2 # put l2 in new list
                list2 = list2.next # make l2 go forward
            temp = temp.next # move the new list go forward
        temp.next = list1 if list1 else list2 # push other leftover values as they are already sorted
        return head.next
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/1759318990/