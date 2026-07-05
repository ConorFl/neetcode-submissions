# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 or list2
        # if list1 is None and list2 is None:
        #     return None
        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1

        # get new head (which is also new tail)
        if list1.val < list2.val:
            new_head = list1
            new_tail = new_head
            list1 = list1.next
        else:
            new_head = list2
            new_tail = new_head
            list2 = list2.next

        while list1 and list2:
            # keep adding to new tail (and move tail)
            if list1.val < list2.val:
                new_tail.next = list1
                new_tail = new_tail.next
                list1 = list1.next
            else:
                new_tail.next = list2
                new_tail = new_tail.next
                list2 = list2.next


        # when one empties, attach the other to tail
        if list1 is None:
            new_tail.next = list2
        else:
            new_tail.next = list1
        
        # return new head
        return new_head
        