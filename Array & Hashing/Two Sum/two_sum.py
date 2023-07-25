
class Solution(object):

    def two_sum_SS(self, nums:list, target:int)-> list:

        # Convert list to dictionary with items' indices as keys
        result_dict = {}

        for index, item in enumerate(nums):
            search_value = target - item
            if search_value in result_dict:
                return [result_dict[search_value] ,index]

            result_dict[item] = index

    def two_sum_neat(self, nums:list, target:int)-> list:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

# Guide for solution:

# Brute Force: Scan all combinations time O(n2), space O(1)
# Hash Map: time complexity O(n) and space O(n)

### Golden rule: Initializing hashmap to empty we are eliminating to reuse same element. Instead of checking all combination, the smart way is to only search the value we are looking for each step.