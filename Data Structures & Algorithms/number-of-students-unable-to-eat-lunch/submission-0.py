class LL:
    def __init__(self, val):
        self.val
        self.next = None


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)
        remaining = len(sandwiches)

        for sandwich in sandwiches:
            loops = 0
            while loops < n and q[0] != sandwich:
                curr = q.popleft()
                q.append(curr)
                loops += 1

            if q[0] == sandwich:
                q.popleft()
                remaining -= 1
            else:
                break

        return remaining