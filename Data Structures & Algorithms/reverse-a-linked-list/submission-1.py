# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: do we need this?
        if head is None:
            return None
        
        # Collect all the nodes
        nodes = []
        curr = head
        while curr is not None:
            nodes.append(curr)
            curr = curr.next

        # Sew them back together in reverse
        new_head = nodes[-1]
        curr_tail = nodes.pop()
        while nodes:
            curr_tail.next = nodes.pop()
            curr_tail = curr_tail.next

        # clean out tail
        curr_tail.next = None

        # return new head
        return new_head