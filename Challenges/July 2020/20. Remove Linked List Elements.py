# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        walker = head
        while(walker!=None and walker.next!=None):
            if(walker.next.val==val):
                walker.next = walker.next.next
            else:
                walker = walker.next
        return head if head==None or head.val!=val else head.next