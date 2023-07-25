import collections

class Solution(object):

    def group_anagrams_SS(self, str_list:list):
        
        ans = collections.defaultdict(list)
        
        for word in str_list:
            char_keys = [0] * 26
            for char in word:
                char_keys[ord(char) - ord("a")] += 1

            ans[tuple(char_keys)].append(word)
            
        return list(ans.values())
            
    def group_anagrams_neat(self, str_list:list)-> list:

        pass


# Guide for solution:

# Sorting: Time O(m.nlogn)
# Hash Map: Time O(m.n)

### Golden rule: Each word can hash as values from (0-26) which is number of repating letters. In python Tuple can be key of dict. defaultdict(list) is for if key is not in dict create and append.