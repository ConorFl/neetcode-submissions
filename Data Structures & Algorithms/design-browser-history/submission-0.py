class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        

    def visit(self, url: str) -> None:
        # Create new node, attach both sides to self.curr
        new_node = Node(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = new_node
        

    def back(self, steps: int) -> str:
        # Loop back `steps` times unless I can't, keep moving self.curr
        for _ in range(steps):
            # We want to move back further but we can't!
            if self.curr.prev is None:
                return self.curr.val
            else:
                self.curr = self.curr.prev
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        # Loop forwaard `steps` times unless I can't, keep moving self.curr
        for _ in range(steps):
            # We want to move forward further but we can't!
            if self.curr.next is None:
                return self.curr.val
            else:
                self.curr = self.curr.next
        return self.curr.val
        


# back / forward positive ints? sure
# visit valid url? doesn't matter
# does initializing a browser history visit the homepage? yes

# stretch: store size to just to head / tail when forward / back greater than num elements

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)