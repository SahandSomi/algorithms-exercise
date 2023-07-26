import pytest
import time
from collections import Counter

class Solution(object):

    def product_of_array_except_self_SS(self, nums:list)-> list:

        answer = {}

        temp_multiplication = 1

        for idx in range(len(nums)):

            answer[idx] = answer.get(idx,0) + temp_multiplication
            temp_multiplication = nums[idx] * temp_multiplication

        temp_multiplication = 1

        for idx in range(len(nums)-1,-1,-1):

            answer[idx] = answer[idx] * temp_multiplication
            temp_multiplication = nums[idx] * temp_multiplication

        return list(answer.values())
    
    def product_of_array_except_self_neat(self, nums:list)-> list:

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    






# Guide for solution:

# Division Operations: Using division is really easy. Take product of all values and divide by value of i. O(2n), memory O(1)

# Two Pass Solver: Since we are only looking for values after and before i. We can have 2 list/Dict that keep track of multiplication values. O(2n), memory(n)

# Two pass Solver in place: calculate two pass in answer array

### Golden rule: Consider option of in-place calculation to optimize memeory.