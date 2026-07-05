class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = Node(-1, None, None)
        self.dummy_tail = Node(-1, None, None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get_node(self, index: int) -> Optional[Node]:
        prev = self.dummy_head
        curr = self.dummy_head.next # could be tail!
        
        for _ in range(index):
            if curr.next is None:
                return None
            else:
                prev = curr
                curr = curr.next
        print("returning", curr.val)
        return curr


    def get(self, index: int) -> int:
        print('get called for index', index)
        node = self.get_node(index)
        print('get got val', node.val if node else 'empty')
        if node:
            return node.val
        else:
            return -1

        

    def addAtHead(self, val: int) -> None:
        prev_head = self.dummy_head.next # could be tail!
        new_node = Node(val, None, None)
        # connect dummy head and new node
        self.dummy_head.next = new_node
        new_node.prev = self.dummy_head
        # connect new node and prev head
        new_node.next = prev_head
        prev_head.prev = new_node
        

    def addAtTail(self, val: int) -> None:
        prev_tail = self.dummy_tail.prev # could be head!
        new_node = Node(val, None, None)
        # connect prev tail and new node
        prev_tail.next = new_node
        new_node.prev = prev_tail
        # connect new node and dummy tail
        new_node.next = self.dummy_tail
        self.dummy_tail.prev = new_node
    

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.get_node(index)
        if node:
            prev = node.prev
            new_node = Node(val, None, None)
            # connect prev and new node
            prev.next = new_node
            new_node.prev = prev
            # connect new node and node
            new_node.next = node
            node.prev = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        node = self.get_node(index)
        if node and node.next: # don't delete if node is dummy_tail!
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)