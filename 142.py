# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        marked = []
        pointer = head
        while (pointer != None):
            if pointer in marked:
                return pointer
            marked.append(pointer)
            pointer = pointer.next
        return None