import pytest

class Solution(object):

    def Trapping_rain_water_SS(self, numbers):

        left, right = 0, 1
        result = 0

        while left == len(numbers) and right == len(numbers):


            if numbers[left] == 0:
                left += 1

            if numbers[right] == 0:
                right += 1

            if numbers[right] >= numbers[left]:
                right = left
                left += 1


            
    
    def Trapping_rain_water_neat(self, nums):
        
        pass
            
# Guide for solution:
# Brute Force: 
# 
### Golden rule: 