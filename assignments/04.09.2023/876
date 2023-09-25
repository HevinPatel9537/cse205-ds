# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0
       
        while current != None:
            count = count + 1
            current = current.next

        ans = head
        
        for i in range(count//2):
                ans= ans.next
        
        return ans
        
        