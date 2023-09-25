# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        current = head = ListNode()
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current.next = list1
                current = list1 
                list1 = list1.next
                

            else:
                current.next = list2
                current = list2
                list2 = list2.next
                


        if list1 != None or list2 != None:
            if list1 != None:
                current.next = list1
            else:
                current.next = list2 

        return head.next
        
        