import pytest
from collections import deque

class Solution(object):

    def Sliding_Window_Maximum_SS(self, nums, k: int) :

        l = r = 0
        q = deque()
        result = []

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                result.append(nums[q[0]])
                l += 1
            
            r += 1
            
        return result
            
# Guide for solution:
# Brute Force: check every combinations O(nk)
# monotonic decreasing deque O(n)
### Golden rule: 