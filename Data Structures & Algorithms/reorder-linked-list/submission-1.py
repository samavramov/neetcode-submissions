# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of linked list
        mid, fast, = head, head

        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        temp = mid.next
        mid.next = None
        # reverse second half
        prev, curr = None, temp
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        revhead = prev
        # append reversed half
        curr = head
        while curr and revhead:
            temp = curr.next
            revtemp = revhead.next
            curr.next = revhead
            curr.next.next = temp
            revhead = revtemp
            curr = temp

        
            




        