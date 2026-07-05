import functools

class Solution:
    @functools.cache
    def climbStairs(self, n: int) -> int:
        # Base case
        if n <= 2:
            return n

        # Recursive
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        