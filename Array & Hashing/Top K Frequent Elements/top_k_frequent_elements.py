import collections

class Solution(object):

    def top_k_frequent_elements_SS(self, nums_list:list, k:int):
        
        count_key = {}

        for i in nums_list:
            count_key[i] = count_key.get(i,0) + 1
        
        count_key =sorted(count_key)
        
        return(count_key[:k])
            
    def top_k_frequent_elements_neat(self, nums_list:list, k:int)-> list:

        count = {}
        freq = [[] for i in range(len(nums_list)+1)]

        for n in nums_list:
            count[n] = 1+ count.get(n,0)
        
        for n,c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1,0, -1):
            for  n in freq[i]:
                res.append(n)
                if len(res) == k:

                    return res




# Guide for solution:

# Bucket Sort: count-values key pair (O(n)).
# Max Heap: pop from heap for k time. pop complexity in heap klogn

### Golden rule: heap are good structure to track max or min value.