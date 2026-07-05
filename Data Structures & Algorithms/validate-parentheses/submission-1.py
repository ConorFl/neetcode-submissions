class Solution:
    def isValid(self, s: str) -> bool:
        open_parens = { '[', '{', '(' }
        matches = { ']': '[', '}': '{', ')': '(' }
        stack = []
        for char in s:
            # open paren -> add to stack
            if char in open_parens:
                stack.append(char)
            # close paren -> check if matching (and pop) otherwise false
            else:
                if len(stack) > 0 and matches[char] == stack[-1]:
                    # match! pop open paren from stack
                    stack.pop()
                else:
                    return False
        # make sure empty!
        return len(stack) == 0