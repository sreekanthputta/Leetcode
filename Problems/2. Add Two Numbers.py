# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l1temp = l1
        l2temp = l2
        l1prev = None
        while(l1temp != None and l2temp != None):
            digitSum = l1temp.val + l2temp.val + carry
            print(l1temp.val, l2temp.val, digitSum, carry)
            l1temp.val = digitSum%10
            carry = floor(digitSum/10)
            l1prev = l1temp
            l1temp = l1temp.next
            l2temp = l2temp.next
            print(l1)
           
        if(l1temp == None):
            l1prev.next = l2temp
            l1temp = l2temp
            
        while(l1temp!=None and carry==1):
            if(l1temp.val==9):
                l1temp.val=0
                l1prev = l1temp
                l1temp = l1temp.next
            else:
                l1temp.val += carry
                carry = 0
                
        if(carry==1):
            l1prev.next = ListNode(carry)
    
        return l1