import pytest
import math
import time
class Solution(object):

    def valid_palindrome_SS(self, str):
        str_ans = ""
        for i in str:
            if i.isalnum():
                str_ans += i.lower()

        if len(str_ans) == 0:
            return True
        
        else:
        
            if len(str_ans)%2 == 0:
                for i in range(math.floor(len(str_ans)/2)):
                    if str_ans[i] != str_ans[len(str_ans)-i-1]:
                        return False
                    
        return True

    
    def valid_palindrome_neat(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

# Guide for solution:
# Solution 1: reverse string in python str[::-1] extra memory, O(3n)
# Solution 2: constant memory using pointer : left pointer and right pointer. time complexity O(n)

### Golden rule: 