# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head):
            val = head.val * 2
            if head.next:
                val += helper(head.next)
            head.val = val % 10
            return val // 10
        val = helper(head)
        if val:
            return ListNode(val, head)
        return head