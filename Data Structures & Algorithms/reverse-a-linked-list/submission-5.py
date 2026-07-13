# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before=None
        curr=head
        if head is None:
            return
        after=head.next
        while curr is not None:
            curr.next=before
            before=curr
            curr=after
            if after is not None:
                after=after.next
        return before