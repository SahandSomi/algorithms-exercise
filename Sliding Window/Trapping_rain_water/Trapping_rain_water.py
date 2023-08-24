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

            
    
    def Trapping_rain_water_neat(self, nums):
        
        pass
            
# Guide for solution:
# Brute Force: 
# 
### Golden rule: 

answer = Solution()
answer.Trapping_rain_water_SS([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])