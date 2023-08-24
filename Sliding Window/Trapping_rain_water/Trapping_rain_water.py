import pytest
from heapq import heapify, heappush, heappop

class Solution(object):

    def Trapping_rain_water_SS(self, numbers):

        result = 0
        heap_left = heapq.heapify([0])
        heap_left = heapq.heapify(numbers)

        for idx in range(0,len(numbers)-1):

            if len(numbers[:idx]) == 0:
                left_min = 0

            else:
                left_min = max(numbers[:idx])

            if len(numbers[idx+1:]) == 0:
                right_min = 0

            else:
                right_min = max(numbers[idx+1:])

            if  min(left_min, right_min) - numbers[idx] > 0 :
                result += min(left_min, right_min) - numbers[idx]


        return result

            
    
    def Trapping_rain_water_neat(self, nums):
        
        pass
            
# Guide for solution:
# Brute Force: 
# 
### Golden rule: 