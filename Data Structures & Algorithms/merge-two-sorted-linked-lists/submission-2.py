# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0)
        temp=d
        temp1=list1
        temp2=list2
        while temp1 is not None and temp2 is not None:
            if temp1.val<=temp2.val:
                temp.next=temp1
                temp=temp.next
                temp1=temp1.next
            else:
                temp.next=temp2
                temp=temp.next
                temp2=temp2.next
        if temp1 is not None:
            temp.next=temp1
        else:
            temp.next=temp2
        return d.next
