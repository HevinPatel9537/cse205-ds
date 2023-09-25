# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        count = 0

        while curr != None:
            count += 1
            curr = curr.next


        if count == n:
            return head.next

        temp = count - n - 1
        curr = head

        for i in range(temp):
            curr = curr.next
            
        curr.next = curr.next.next

        return head


