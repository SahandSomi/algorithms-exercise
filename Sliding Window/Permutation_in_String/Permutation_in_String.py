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
    
    def Permutation_in_String_neat(self, s):
        
        pass
            
# Guide for solution:
# Brute Force: check every combinations O(n2)
# Two Pointer moving O(n)
### Golden rule: Edge cases don't forgot those