import pytest
import time
from collections import Counter

class Solution(object):

    def valid_anagram_SS(self, s:str, t:str)-> bool:

        if len(s) != len(t):
            return False

        else:
            letter_count = {}
            for char in s:
                letter_count[char] = letter_count.get(char, 0) + 1

            for char in t:
                if char in letter_count:
                    letter_count[char] -= 1
                    if letter_count[char] < 0:
                        return False
                else:
                    return False
                
            return True

    def valid_anagram_neat(self, s:str, t:str)-> bool:
        return Counter(s) == Counter(t)

# Guide for solution:

# Hash Map: time complexity O(T+S) and space O(T+S)
# Sorting: Time complexity O(nlogn) and space O(1) or O(n) and compare two string

### Golden rule: For dict in python .get is used if key is not exist. Counter is build-in hash map for counting in python.