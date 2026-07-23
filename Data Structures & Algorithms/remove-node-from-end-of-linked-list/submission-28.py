# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        if length == 1 or length == 0:
            return None
        if n == length:
            return head.next
        dummy = head
        for i in range(length-n-1):
            dummy = dummy.next
        dummy.next = dummy.next.next
        return head


    

        