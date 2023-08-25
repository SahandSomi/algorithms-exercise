import pytest
from heapq import heapify, heappush, heappop, _heapify_max,_heappop_max
class Solution(object):

    def Trapping_rain_water_SS(self, numbers):

        result = 0
        heap_left = [0]
        _heapify_max(heap_left)

        heap_right =[i for i in numbers]
        _heapify_max(heap_right)

        seen_number = {}

        for idx in range(0,len(numbers)-1):

            left_max = heap_left[0]

            while heap_right[0] in seen_number:

                if seen_number[heap_right[0]]>1:

                    seen_number[heap_right[0]] -= 1
                else:
                    seen_number.pop(heap_right[0])

                _heappop_max(heap_right)

                    
            right_max = heap_right[0]
           
            if min(left_max, right_max) - numbers[idx] > 0 :
                result += min(left_max, right_max) - numbers[idx]

            heappush(heap_left, numbers[idx])
            _heapify_max(heap_left)
            seen_number[numbers[idx]] = seen_number.get(numbers[idx], 0) + 1


        return result

            
    
    def Trapping_rain_water_neat(self, height):
        
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
            
# Guide for solution:
# Brute Force: 
# 
### Golden rule: 