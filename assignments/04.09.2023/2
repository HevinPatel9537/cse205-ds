# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        res = dummy
    
        carry = 0 

        while l1 or l2:
            v1 = 0
            v2 = 0 
            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            val = v1 + v2 + carry
            res.next = ListNode(val%10)
            res = res.next
            carry = val//10

            if carry != 0:
                res.next = ListNode(carry)
                
        return dummy.next 
        
        