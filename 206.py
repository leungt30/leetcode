# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeList = []
        current = head
        if (current == None):
            return head
        while (current != None):
            nodeList.append(current.val)
            current = current.next 
       
        
   
        fakeHead = ListNode()
        fakeHead.val = nodeList[-1]
        current = fakeHead
        for i in range(len(nodeList)-1):
            n = ListNode()
            n.val = nodeList[-i-2]
            current.next = n
            current = n
            

    


        return fakeHead
