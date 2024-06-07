# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        final = None
        carry = 0
        while (l1 or l2 or carry):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            xval = sum % 10
            new_node = ListNode(xval)
            if final is None:
                head = new_node
                final = new_node

            else:
                final.next = new_node
                final = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head