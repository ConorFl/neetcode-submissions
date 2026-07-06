# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if len(lists) == 0:
        #     return None

        dummy_head = ListNode(-1, None)
        curr_tail = dummy_head

        min_heap = [NodeWrapper(l) for l in lists if l]
        heapq.heapify(min_heap)
        print(min_heap)
        while min_heap:
            min_list_wrapper = heapq.heappop(min_heap)
            new_node = min_list_wrapper.node
            min_list = new_node.next
            curr_tail.next = new_node
            new_node.next = None
            curr_tail = new_node
            if min_list:
                heapq.heappush(min_heap, NodeWrapper(min_list))

        return dummy_head.next        

            # attach to curr (rememeber to fix nexts)
            # push min_list back into heap

        # double check if empty and just have dummy_head -> dummy_tail?
        # remove dummy_tail!