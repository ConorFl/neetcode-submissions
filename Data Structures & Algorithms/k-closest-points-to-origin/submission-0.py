import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # store a max heap of the k closest
        max_heap = [] # (-dist, point)
        # for the first k elements just push on
        # for the remaining elements, compare with the top (max) element
        for point in points:
            dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, point))
            else:
                # pop and push if it's closer
                if dist < -max_heap[0][0]:
                    heapq.heapreplace(max_heap, (-dist, point))
        # return heap (points in heap)
        return [p[1] for p in max_heap]