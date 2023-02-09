# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        pointer = head
        # if (list1.val > list2.val):
        #     head = list2
        # else
        #     head = list1

        cur1 = list1
        cur2 = list2

        while (cur1 != None and cur2 != None):
            if (cur1.val < cur2.val):
                pointer.next = cur1
                
                cur1 = cur1.next
            else:
                pointer.next = cur2
                cur2 = cur2.next
            pointer = pointer.next
        if (cur1 == None):
            pointer.next = cur2
        elif (cur2 == None):
            pointer.next = cur1
        return head.next

            
            