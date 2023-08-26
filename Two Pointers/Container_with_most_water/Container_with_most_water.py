import pytest

class Solution(object):

    def Container_with_most_water_SS(self, numbers):

        left , right = 0 , len(numbers)-1
        max_area = 0
        while left< right:
            temp_area = min(numbers[right],numbers[left])*(right-left)
            if numbers[left] >=numbers[right]:
                right -= 1
            else:
                left += 1

            max_area = max(temp_area,max_area)

        return max_area
    
    def Container_with_most_water_neat(self, nums):
        
        pass
            
# Guide for solution:
# Brute Force: check every combinations O(n2)
# Two Pointer O(n)
### Golden rule: two pointer to check best combanition according to rules like keep big value and move other pointer. According to Leetcode if is faster than min.