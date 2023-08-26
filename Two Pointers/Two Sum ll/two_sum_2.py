import pytest

class Solution(object):

    def two_sum_2_SS(self, numbers, target):

        for index, value in enumerate(numbers):
            number_1 = value
            number_2 = target - number_1
            index_1 = index

            for j in range(index_1,len(numbers)):
                if numbers[j] > number_2:
                    break
                if number_2 == numbers[j]:
                    return [index_1+1,j+1]

    
    def two_sum_2_neat(self, numbers, target):
        l , r = 0, len(numbers)-1

        while l<r:

            curSum = numbers[l]+numbers[r]

            if curSum > target: 
                r -= 1

            
            elif curSum < target:
                l += 1

            else:

                return [l+1, r+1]
# Guide for solution:
# Brute Force: Check all combination with itertool.combination O(n2)
# Since it is sorted we can use two pinter we can have second pointer from last O(n)

### Golden rule: consider two pointer that considering feasible solutions