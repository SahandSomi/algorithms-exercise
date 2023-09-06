import pytest

class Solution(object):

    def Permutation_in_String_SS(self, s1: str, s2: str):

        l = 0
        s1_dict = {}
        s2_dict = {}

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1_dict[s1[i]] = 1 + s1_dict.get(s1[i], 0)

        for i in range(len(s1)):
            s2_dict[s2[i]] = 1 + s2_dict.get(s2[i], 0)

        if s2_dict == s1_dict:
            return True

        else:
            s2_dict[s2[l]] -= 1

            if s2_dict[s2[l]] == 0:
                del s2_dict[s2[l]]

            l+=1

            for r in range(len(s1), len(s2)):

                s2_dict[s2[r]] = 1 + s2_dict.get(s2[r], 0)

                if s2_dict == s1_dict:
                    return True
                
                else:
                    s2_dict[s2[l]] -= 1

                    if s2_dict[s2[l]] == 0:
                        del s2_dict[s2[l]]

                    l+=1

            return False
    
    def Permutation_in_String_neat(self, s1,s2):
        
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
            
# Guide for solution:
# Brute Force: check every combinations O(n2)
# Two Pointer moving O(n)
### Golden rule: Edge cases don't forgot those