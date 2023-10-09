# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(), ListNode()
        before_now, after_now = before, after
        
        while head:
            if head.val < x:
                before_now.next, before_now = head, head
            else:
                after_now.next, after_now = head, head
            head = head.next
        
        after_now.next = None
        before_now.next = after.next
        return before.next