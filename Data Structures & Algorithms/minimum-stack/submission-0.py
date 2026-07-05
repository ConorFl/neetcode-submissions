class MinStack:

    def __init__(self):
        self.stack = []
        self.mins_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.mins_stack.append(val)
        else:
            self.mins_stack.append(min(val, self.mins_stack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.mins_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins_stack[-1]
