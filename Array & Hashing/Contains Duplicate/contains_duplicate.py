import pytest
import time
class Solution(object):
    def containsDuplicate_SS(self, nums):
        num_dict = {}

        for i in nums:
            num_dict[i] = num_dict.get(i,0) + 1
            if num_dict[i] >= 2:
                return True
            
        return False
    
    def containsDuplicate_neat(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

def test():
    answer = Solution()
    assert answer.containsDuplicate_SS([1,2,3,1]) == True
    assert answer.containsDuplicate_SS([1,2,3,4]) == False
    assert answer.containsDuplicate_SS([1,1,1,3,3,4,3,2,4,2]) == True

# Guide for solution:
# Brute Force: Compare each element to every other element to find duplicates. This means the time complexity is O(n**2) and the space complexity is O(1).
# Sorting: Sort the array and check adjacent values for any duplicates. This has a time complexity of O(nlogn) and a space complexity of O(1).
# Hashing: Traverse the array and add each value to a hash table (e.g., a dictionary or a set), checking if the value has already been added. This has a time complexity of O(n) and a space complexity of O(n).

### Golden rule: When checking for duplicates in an array, it is better to use a hash table (i.e., a dictionary or a set) since searching is O(1) and Python has built-in support for these data structures.