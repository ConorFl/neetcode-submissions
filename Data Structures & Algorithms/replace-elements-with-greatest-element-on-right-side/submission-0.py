class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # store last elem as max, replace with -1
        max_elem = arr[-1]
        arr[-1] = -1

        # loop backwards replace with max
        for idx in range(len(arr) - 2, -1, -1):
            curr_elem = arr[idx]
            arr[idx] = max_elem
        # see if replaced val should be new max
            if curr_elem > max_elem:
                max_elem = curr_elem
        # return list
        return arr
# Test 1 elem, 2 elem