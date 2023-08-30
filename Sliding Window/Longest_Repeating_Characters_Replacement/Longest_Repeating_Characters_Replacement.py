import pytest

class Solution(object):

    def Longest_Repeating_Characters_Replacement_SS(self, s, k):

        l = 0
        hash_letter = {}
        maxf = 0
        res = 0

        for r in range(len(s)):

            hash_letter[s[r]] = 1 + hash_letter.get(s[r], 0)

            if hash_letter[s[r]]> maxf:
                maxf = hash_letter[s[r]]

            if (r-l+1) - maxf <= k:
                res = r-l+1

            else:
                while (r-l+1) - maxf > k and l<=r:
                    hash_letter[s[l]] -= 1
                    l += 1

        return res
    
    def Longest_Repeating_Characters_Replacement_neat(self, s, k):
        
        count = {}
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
            
# Guide for solution:
# Brute Force: check every combinations O(n2)
# Window rolling with two pointer moving O(n)
### Golden rule: 