import pytest

class Solution(object):

    def Longest_Substring_Without_Repeating_Characters_SS(self, s):

        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length
    
    def Longest_Substring_Without_Repeating_Characters_neat(self, s):
        
        CharSet = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in CharSet:
                CharSet.remove(s[l])
                l += 1

            CharSet.add(s[r])
            
            if result <= (r-l+1):

                result = (r-l+1)

        return result
            
# Guide for solution:
# Brute Force: check every combinations O(n2)
# Two Pointer moving O(n)
### Golden rule: 